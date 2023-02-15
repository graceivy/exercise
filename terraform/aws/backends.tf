terraform {
  cloud {
    organization = "pingping"

    workspaces {
      name = "dev"
    }
  }
}
