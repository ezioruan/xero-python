# coding: utf-8

"""
    Xero AppStore API

    These endpoints are for Xero Partners to interact with the App Store Billing platform  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""

"""
    OpenAPI spec version: 2.27.0
"""

import importlib
import re  # noqa: F401

from xero_python import exceptions
from xero_python.api_client import ApiClient, ModelFinder

try:
    from .exception_handler import translate_status_exception
except ImportError:
    translate_status_exception = exceptions.translate_status_exception


class empty:
    """empty object to mark optional parameter not set"""


class AppStoreApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    base_url = "https://api.xero.com/appstore/2.0"
    models_module = importlib.import_module("xero_python.appstore.models")

    def __init__(self, api_client=None, base_url=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_resource_url(self, resource_path):
        """
        Combine API base url with resource specific path
        :param str resource_path: API endpoint specific path
        :return: str full resource path
        """
        return self.base_url + resource_path

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    def get_subscription(
        self,
        subscription_id,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Retrieves a subscription for a given subscriptionId  # noqa: E501
        OAuth2 scope: marketplace.billing
        :param str subscription_id: Unique identifier for Subscription object (required)
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: Subscription
        """

        # verify the required parameter 'subscription_id' is set
        if subscription_id is None:
            raise ValueError(
                "Missing the required parameter `subscription_id` "
                "when calling `get_subscription`"
            )

        collection_formats = {}
        path_params = {
            "subscriptionId": subscription_id,
        }

        query_params = []

        header_params = {}

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/subscriptions/{subscriptionId}")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="Subscription",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_subscription")
