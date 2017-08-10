import requests
import json

payload = '''{
  "ref": "refs/heads/master",
  "before": "23de2890bbe26d4be18a44b067d28759e7f67bcd",
  "after": "d5612493fd2fc58a6b93e8c510a1a2157445fed1",
  "created": false,
  "deleted": false,
  "forced": false,
  "base_ref": null,
  "compare": "https://github.com/Azure/azure-cli/compare/23de2890bbe2...d5612493fd2f",
  "commits": [
    {
      "id": "d5612493fd2fc58a6b93e8c510a1a2157445fed1",
      "tree_id": "ffc3eddd513037d9dc6024fde8483b97a251e914",
      "distinct": true,
      "message": "Add message that 'az component' commands will be deprecated (#4193)",
      "timestamp": "2017-08-10T12:18:09-07:00",
      "url": "https://github.com/Azure/azure-cli/commit/d5612493fd2fc58a6b93e8c510a1a2157445fed1",
      "author": {
        "name": "Derek Bekoe",
        "email": "debekoe@microsoft.com",
        "username": "derekbekoe"
      },
      "committer": {
        "name": "GitHub",
        "email": "noreply@github.com",
        "username": "web-flow"
      },
      "added": [

      ],
      "removed": [

      ],
      "modified": [
        "src/command_modules/azure-cli-component/HISTORY.rst",
        "src/command_modules/azure-cli-component/azure/cli/command_modules/component/custom.py"
      ]
    }
  ],
  "head_commit": {
    "id": "d5612493fd2fc58a6b93e8c510a1a2157445fed1",
    "tree_id": "ffc3eddd513037d9dc6024fde8483b97a251e914",
    "distinct": true,
    "message": "Add message that 'az component' commands will be deprecated (#4193)",
    "timestamp": "2017-08-10T12:18:09-07:00",
    "url": "https://github.com/Azure/azure-cli/commit/d5612493fd2fc58a6b93e8c510a1a2157445fed1",
    "author": {
      "name": "Derek Bekoe",
      "email": "debekoe@microsoft.com",
      "username": "derekbekoe"
    },
    "committer": {
      "name": "GitHub",
      "email": "noreply@github.com",
      "username": "web-flow"
    },
    "added": [

    ],
    "removed": [

    ],
    "modified": [
      "src/command_modules/azure-cli-component/HISTORY.rst",
      "src/command_modules/azure-cli-component/azure/cli/command_modules/component/custom.py"
    ]
  },
  "repository": {
    "id": 51040886,
    "name": "azure-cli",
    "full_name": "Azure/azure-cli",
    "owner": {
      "name": "Azure",
      "email": "opensource@microsoft.com",
      "login": "Azure",
      "id": 6844498,
      "avatar_url": "https://avatars0.githubusercontent.com/u/6844498?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/Azure",
      "html_url": "https://github.com/Azure",
      "followers_url": "https://api.github.com/users/Azure/followers",
      "following_url": "https://api.github.com/users/Azure/following{/other_user}",
      "gists_url": "https://api.github.com/users/Azure/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/Azure/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/Azure/subscriptions",
      "organizations_url": "https://api.github.com/users/Azure/orgs",
      "repos_url": "https://api.github.com/users/Azure/repos",
      "events_url": "https://api.github.com/users/Azure/events{/privacy}",
      "received_events_url": "https://api.github.com/users/Azure/received_events",
      "type": "Organization",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/Azure/azure-cli",
    "description": "Command-line tools for Azure.",
    "fork": false,
    "url": "https://github.com/Azure/azure-cli",
    "forks_url": "https://api.github.com/repos/Azure/azure-cli/forks",
    "keys_url": "https://api.github.com/repos/Azure/azure-cli/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/Azure/azure-cli/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/Azure/azure-cli/teams",
    "hooks_url": "https://api.github.com/repos/Azure/azure-cli/hooks",
    "issue_events_url": "https://api.github.com/repos/Azure/azure-cli/issues/events{/number}",
    "events_url": "https://api.github.com/repos/Azure/azure-cli/events",
    "assignees_url": "https://api.github.com/repos/Azure/azure-cli/assignees{/user}",
    "branches_url": "https://api.github.com/repos/Azure/azure-cli/branches{/branch}",
    "tags_url": "https://api.github.com/repos/Azure/azure-cli/tags",
    "blobs_url": "https://api.github.com/repos/Azure/azure-cli/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/Azure/azure-cli/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/Azure/azure-cli/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/Azure/azure-cli/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/Azure/azure-cli/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/Azure/azure-cli/languages",
    "stargazers_url": "https://api.github.com/repos/Azure/azure-cli/stargazers",
    "contributors_url": "https://api.github.com/repos/Azure/azure-cli/contributors",
    "subscribers_url": "https://api.github.com/repos/Azure/azure-cli/subscribers",
    "subscription_url": "https://api.github.com/repos/Azure/azure-cli/subscription",
    "commits_url": "https://api.github.com/repos/Azure/azure-cli/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/Azure/azure-cli/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/Azure/azure-cli/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/Azure/azure-cli/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/Azure/azure-cli/contents/{+path}",
    "compare_url": "https://api.github.com/repos/Azure/azure-cli/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/Azure/azure-cli/merges",
    "archive_url": "https://api.github.com/repos/Azure/azure-cli/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/Azure/azure-cli/downloads",
    "issues_url": "https://api.github.com/repos/Azure/azure-cli/issues{/number}",
    "pulls_url": "https://api.github.com/repos/Azure/azure-cli/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/Azure/azure-cli/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/Azure/azure-cli/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/Azure/azure-cli/labels{/name}",
    "releases_url": "https://api.github.com/repos/Azure/azure-cli/releases{/id}",
    "deployments_url": "https://api.github.com/repos/Azure/azure-cli/deployments",
    "created_at": 1454545311,
    "updated_at": "2017-08-10T07:47:36Z",
    "pushed_at": 1502392690,
    "git_url": "git://github.com/Azure/azure-cli.git",
    "ssh_url": "git@github.com:Azure/azure-cli.git",
    "clone_url": "https://github.com/Azure/azure-cli.git",
    "svn_url": "https://github.com/Azure/azure-cli",
    "homepage": null,
    "size": 24997,
    "stargazers_count": 485,
    "watchers_count": 485,
    "language": "Python",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false, "forks_count": 249,
    "mirror_url": null,
    "open_issues_count": 552,
    "forks": 249,
    "open_issues": 552,
    "watchers": 485,
    "default_branch": "master",
    "stargazers": 485,
    "master_branch": "master",
    "organization": "Azure"
  },
  "pusher": {
    "name": "derekbekoe",
    "email": "debekoe@microsoft.com"
  },
  "organization": {
    "login": "Azure",
    "id": 6844498,
    "url": "https://api.github.com/orgs/Azure",
    "repos_url": "https://api.github.com/orgs/Azure/repos",
    "events_url": "https://api.github.com/orgs/Azure/events",
    "hooks_url": "https://api.github.com/orgs/Azure/hooks",
    "issues_url": "https://api.github.com/orgs/Azure/issues",
    "members_url": "https://api.github.com/orgs/Azure/members{/member}",
    "public_members_url": "https://api.github.com/orgs/Azure/public_members{/member}",
    "avatar_url": "https://avatars0.githubusercontent.com/u/6844498?v=4",
    "description": "APIs, SDKs and open source projects from Microsoft Azure"
  },
  "sender": {
    "login": "derekbekoe",
    "id": 16448634,
    "avatar_url": "https://avatars3.githubusercontent.com/u/16448634?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/derekbekoe",
    "html_url": "https://github.com/derekbekoe",
    "followers_url": "https://api.github.com/users/derekbekoe/followers",
    "following_url": "https://api.github.com/users/derekbekoe/following{/other_user}",
    "gists_url": "https://api.github.com/users/derekbekoe/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/derekbekoe/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/derekbekoe/subscriptions",
    "organizations_url": "https://api.github.com/users/derekbekoe/orgs",
    "repos_url": "https://api.github.com/users/derekbekoe/repos",
    "events_url": "https://api.github.com/users/derekbekoe/events{/privacy}",
    "received_events_url": "https://api.github.com/users/derekbekoe/received_events",
    "type": "User",
    "site_admin": false
  }
}
'''
payload = json.loads(payload)

base_url = 'http://localhost:5000/api/build'
response = requests.post(url='{}?client_id={}'.format(base_url, 'build-trigger'), json=payload)
print(response)