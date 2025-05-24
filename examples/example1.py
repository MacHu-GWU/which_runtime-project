# -*- coding: utf-8 -*-

from which_runtime.api import runtime

print(f"{runtime.is_local = }")
# True
print(f"{runtime.is_local_runtime_group = }")
# True
print(f"{runtime.is_gitlab_ci = }")
# False
print(f"{runtime.is_ci_runtime_group = }")
# False
print(f"{runtime.is_aws_lambda = }")
# False
print(f"{runtime.is_app_runtime_group = }")
# False
