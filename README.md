Tanzu Framework Downstream Testing
==================================

This repo contains APIs and Jenkins pipelines, which work together to
test upstream tanzu-framework PRs in downstream.

APIs listen on `/webhook` for incoming Github webhook event.

Required envrionment variables:
- TANZU_FRAMEWORK_REPO_ORG
   Org name / owner of `tanzu-framework` repo (`vmware-tanzu`)
-	GH_WEBHOOK_SECRET
   Github webhook secret, should be same as the one configured on github.com, this is to verify the github webhook event payload.
-	GITHUB_TOKEN
   Github access token with permissions to read repo and teams. This is to verify the trusted reviewer (parsing CODEOWNERS file).
-	JENKINS_USERNAME
   Jenkins username to trigger downstream build.
-	JENKINS_ACCESS_TOKEN
  Jenkins access token to trigger downstream build.
-	GITLAB_API_TOKEN
  Gitlab API token to read current open MRs to verify if the tests for an upstream PR is already running.
- GOPRIVATE should be set up to access repositories under vmware's private network, run:
```Bash
$ go env -w GOPRIVATE=gitlab.eng.vmware.com/tanzu-framework
```
- Setup github config url to use SSH instead of HTTPS url, run:
```Bash
$ git config --global url."git@gitlab.eng.vmware.com:".insteadOf "https://gitlab.eng.vmware.com/"
```
