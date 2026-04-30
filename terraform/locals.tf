locals {
  runtime_environment_variables = merge(
    var.runtime_environment_variables,
    {
      OPENAI_API_KEY      = var.openai_api_key
      NEXT_PUBLIC_API_URL = var.next_public_api_url
    },
  )
}
