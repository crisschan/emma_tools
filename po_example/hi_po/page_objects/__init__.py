#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Map PageElement constructor arguments to webdriver locator enums
_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id_': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class_name': By.CLASS_NAME,
                }


class PageObject(object):
    """Page Object pattern.

    :param webdriver: `selenium.webdriver.WebDriver`
        Selenium webdriver instance
    :param root_uri: `str`
        Root URI to base any calls to the ``PageObject.get`` method. If not defined
        in the constructor it will try and look it from the webdriver object.
    """
    def __init__(self, webdriver, root_uri=None):
        self.driver = webdriver
        self.root_uri = root_uri if root_uri else getattr(self.w, 'root_uri', None)

    def get(self, uri):
        """
        :param uri:  URI to GET, based off of the root_uri attribute.
        """
        root_uri = self.root_uri or ''
        self.driver.get(root_uri + uri)

    def getTitle(self):
        '''

        :return: return the page title
        '''
        return self.driver.title
    def switchTo(self,loc):
        '''
        :param loc: frame or windows name,id and so on
        :return:
        '''
        try:
            self.driver.switch_to.frame(loc)
        except:
            try:
                self.driver.switch_to.windows(loc)
            except:
                print('Error: no can switch to element')

    def acceptAlert(self):
        '''
        accept the alert
        :return:
        '''
        self.driver.switch_to.alert().accept()


class PageElement(object):
    """Page Element descriptor.

    :param css:    `str`
        Use this css locator
    :param id_:    `str`
        Use this element ID locator
    :param name:    `str`
        Use this element name locator
    :param xpath:    `str`
        Use this xpath locator
    :param link_text:    `str`
        Use this link text locator
    :param partial_link_text:    `str`
        Use this partial link text locator
    :param tag_name:    `str`
        Use this tag name locator
    :param class_name:    `str`
        Use this class locator

    :param context: `bool`
        This element is expected to be called with context

    Page Elements are used to access elements on a page. The are constructed
    using this factory method to specify the locator for the element.
        >>> from page_objects import PageObject, PageElement
        >>> class MyPage(PageObject):
                elem1 = PageElement(css='div.myclass')
                elem2 = PageElement(id_='foo')
                elem_with_context = PageElement(name='bar', context=True)

    Page Elements act as property descriptors for their Page Object, you can get
    and set them as normal attributes.
    """
    def __init__(self, context=False, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kwargs.items()))
        self.locator = (_LOCATOR_MAP[k], v)
        self.has_context = bool(context)

    def find(self, context,sleeptime = 10):
        try:
            WebDriverWait(context, sleeptime).until(EC.presence_of_all_elements_located(self.locator))

            return context.find_element(by=self.locator[0], value=self.locator[1])
            #
            # return WebDriverWait(context,sleeptime).until(EC.presence_of_all_elements_located(self.locator))

        except NoSuchElementException:
            return None

    def __get__(self, instance, owner, context=None):
        if not instance:
            return None

        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)

        if not context:
            context = instance.driver

        return self.find(context)

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elem = self.__get__(instance, instance.__class__)
        if not elem:
            raise ValueError("Can't set value, element not found")
        elem.send_keys(value)




class MultiPageElement(PageElement):
    """ Like `PageElement` but returns multiple results.

        >>> from page_objects import PageObject, MultiPageElement
        >>> class MyPage(PageObject):
                all_table_rows = MultiPageElement(tag='tr')
                elem2 = PageElement(id_='foo')
                elem_with_context = PageElement(tag='tr', context=True)
    """
    def find(self, context):
        try:
            return context.find_elements(*self.locator)
        except NoSuchElementException:
            return []

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elems = self.__get__(instance, instance.__class__)
        if not elems:
            raise ValueError("Can't set value, no elements found")
        [elem.send_keys(value) for elem in elems]

class GroupPageElement(MultiPageElement):

    '''
    crisschan modi
    get a group elements,like a dropbox,a group radios
    return is a dic{}
    exp.
    <select class="search_input" id="merviewlevel" name="merviewlevel">
        <option value="">select</option>
        <option value="5">6</option>
        <option value="6">7</option>
        <option value="7">8</option>
        <option value="8">9</option>
        <option value="9">10</option>
    </select>

    merviewlevel=GroupPageElement(xpath='//*[@id="merviewlevel"]/option')

    要选择 商户展示优先级为6
    merviewlevel[u'6'].click()
    '''

    def find(self, context):
        # print context
        try:
            # return context.find_elements(*self.locator)
            dicGroup = {}
            # print context.find_elements(*self.locator)
            for aElement in context.find_elements(*self.locator):
                dicGroup[aElement.text] = aElement
                # print dicGroup
            # print dicGroup
            return dicGroup

        except NoSuchElementException:
            return {}

    def __set__(self, instance, value):
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elems = self.__get__(instance, instance.__class__)
        if not elems:
            raise ValueError("Can't set value, no elements found")
        [elem.send_keys(value) for elem in elems]

# Backwards compatibility with previous versions that used factory methods
page_element = PageElement
multi_page_element = MultiPageElement
