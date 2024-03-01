import re

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class testck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that resources are correctly tagged"
        id = "testck"
        supported_resources = ["*"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources
        )

    def scan_resource_conf(self, conf):
        """
        Looks for tagging config in all resources:
        :return: <CheckResult>
        """
        return CheckResult.FAILED


check = testck()
