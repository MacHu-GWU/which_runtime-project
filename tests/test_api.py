# -*- coding: utf-8 -*-

from which_runtime import api


def test():
    _ = api
    _ = api.USER_RUNTIME_NAME
    _ = api.RunTimeGroupEnum
    _ = api.RunTimeEnum
    _ = api.runtime_emoji_mapper
    _ = api.Runtime
    _ = api.runtime

    _ = api.RunTimeGroupEnum.local.value
    _ = api.RunTimeGroupEnum.ci.value
    _ = api.RunTimeGroupEnum.app.value
    _ = api.RunTimeGroupEnum.unknown.value

    _ = _ = api.RunTimeEnum.local.value
    _ = _ = api.RunTimeEnum.aws_cloud9.value
    _ = _ = api.RunTimeEnum.aws_codebuild.value
    _ = _ = api.RunTimeEnum.github_action.value
    _ = _ = api.RunTimeEnum.gitlab_ci.value
    _ = _ = api.RunTimeEnum.bitbucket_pipeline.value
    _ = _ = api.RunTimeEnum.circleci.value
    _ = _ = api.RunTimeEnum.jenkins.value
    _ = _ = api.RunTimeEnum.aws_lambda.value
    _ = _ = api.RunTimeEnum.aws_batch.value
    _ = _ = api.RunTimeEnum.aws_glue.value
    _ = _ = api.RunTimeEnum.aws_ec2.value
    _ = _ = api.RunTimeEnum.aws_ecs.value
    _ = _ = api.RunTimeEnum.glue_container.value
    _ = _ = api.RunTimeEnum.unknown.value


if __name__ == "__main__":
    from which_runtime.tests import run_cov_test

    run_cov_test(
        __file__,
        "which_runtime.api",
        preview=False,
    )
