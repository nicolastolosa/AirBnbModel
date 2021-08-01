import git

def get_git_hash() -> str:
    repo = git.Repo()
    return repo.head.object.hexsha


# search_parent_directories=True