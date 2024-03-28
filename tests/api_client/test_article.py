# coding: utf-8

"""
    Impresso Public API

    Impresso Public API Documentation

    The version of the OpenAPI document: 2.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from impresso.api_client.models.article import Article

class TestArticle(unittest.TestCase):
    """Article unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Article:
        """Test Article
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Article`
        """
        model = Article()
        if include_optional:
            return Article(
                uid = '',
                type = '',
                title = '',
                size = 56,
                nb_pages = 56,
                pages = [
                    impresso.api_client.models.page.Page(
                        uid = '', 
                        num = 56, 
                        issue_uid = '', 
                        newspaper_uid = '', 
                        iiif = '', 
                        iiif_thumbnail = '', 
                        access_rights = '', 
                        labels = [
                            ''
                            ], 
                        has_coords = True, 
                        has_errors = True, 
                        regions = [
                            None
                            ], 
                        obfuscated = True, 
                        iiif_fragment = '', )
                    ],
                is_cc = True,
                excerpt = '',
                locations = [
                    impresso.api_client.models.entity.Entity(
                        uid = '', 
                        relevance = 56, )
                    ],
                persons = [
                    impresso.api_client.models.entity.Entity(
                        uid = '', 
                        relevance = 56, )
                    ]
            )
        else:
            return Article(
                uid = '',
                type = '',
                title = '',
                size = 56,
                nb_pages = 56,
                pages = [
                    impresso.api_client.models.page.Page(
                        uid = '', 
                        num = 56, 
                        issue_uid = '', 
                        newspaper_uid = '', 
                        iiif = '', 
                        iiif_thumbnail = '', 
                        access_rights = '', 
                        labels = [
                            ''
                            ], 
                        has_coords = True, 
                        has_errors = True, 
                        regions = [
                            None
                            ], 
                        obfuscated = True, 
                        iiif_fragment = '', )
                    ],
                is_cc = True,
                excerpt = '',
        )
        """

    def testArticle(self):
        """Test Article"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()