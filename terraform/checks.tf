check "app_runner_required_env" {
  assert {
    condition     = var.openai_api_key != ""
    error_message = "Set openai_api_key (e.g. export TF_VAR_openai_api_key=...)."
  }
}
