import requests
import json

payload = '''{
  "ref": "refs/heads/master",
  "before": "ab5153a5c2b69ada3dc691e32b60af9912f9ba73",
  "after": "025efffcdbb84eee44ed36024ba556a5f371d333",
  "created": false,
  "deleted": false,
  "forced": false,
  "base_ref": null,
  "compare": "https://github.com/troydai/webhooktest/compare/ab5153a5c2b6...025efffcdbb8",
  "commits": [
    {
      "id": "025efffcdbb84eee44ed36024ba556a5f371d333",
      "tree_id": "e27e35e37d9dd038537a024f5f6b9cc0b545f7fa",
      "distinct": true,
      "message": "update",
      "timestamp": "2017-08-10T14:58:40-07:00",
      "url": "https://github.com/troydai/webhooktest/commit/025efffcdbb84eee44ed36024ba556a5f371d333",
      "author": {
        "name": "Troy Dai",
        "email": "troy.dai@outlook.com",
        "username": "troydai"
      },
      "committer": {
        "name": "Troy Dai",
        "email": "troy.dai@outlook.com",
        "username": "troydai"
      },
      "added": [

      ],
      "removed": [

      ],
      "modified": [
        "test.py"
      ]
    }
  ],
  "head_commit": {
    "id": "025efffcdbb84eee44ed36024ba556a5f371d333",
    "tree_id": "e27e35e37d9dd038537a024f5f6b9cc0b545f7fa",
    "distinct": true,
    "message": "update",
    "timestamp": "2017-08-10T14:58:40-07:00",
    "url": "https://github.com/troydai/webhooktest/commit/025efffcdbb84eee44ed36024ba556a5f371d333",
    "author": {
      "name": "Troy Dai",
      "email": "troy.dai@outlook.com",
      "username": "troydai"
    },
    "committer": {
      "name": "Troy Dai",
      "email": "troy.dai@outlook.com",
      "username": "troydai"
    },
    "added": [

    ],
    "removed": [

    ],
    "modified": [
      "test.py"
    ]
  },
  "repository": {
    "id": 99963968,
    "name": "webhooktest",
    "full_name": "troydai/webhooktest",
    "owner": {
      "name": "troydai",
      "email": "troy.dai@outlook.com",
      "login": "troydai",
      "id": 1329240,
      "avatar_url": "https://avatars2.githubusercontent.com/u/1329240?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/troydai",
      "html_url": "https://github.com/troydai",
      "followers_url": "https://api.github.com/users/troydai/followers",
      "following_url": "https://api.github.com/users/troydai/following{/other_user}",
      "gists_url": "https://api.github.com/users/troydai/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/troydai/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/troydai/subscriptions",
      "organizations_url": "https://api.github.com/users/troydai/orgs",
      "repos_url": "https://api.github.com/users/troydai/repos",
      "events_url": "https://api.github.com/users/troydai/events{/privacy}",
      "received_events_url": "https://api.github.com/users/troydai/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/troydai/webhooktest",
    "description": null,
    "fork": false,
    "url": "https://github.com/troydai/webhooktest",
    "forks_url": "https://api.github.com/repos/troydai/webhooktest/forks",
    "keys_url": "https://api.github.com/repos/troydai/webhooktest/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/troydai/webhooktest/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/troydai/webhooktest/teams",
    "hooks_url": "https://api.github.com/repos/troydai/webhooktest/hooks",
    "issue_events_url": "https://api.github.com/repos/troydai/webhooktest/issues/events{/number}",
    "events_url": "https://api.github.com/repos/troydai/webhooktest/events",
    "assignees_url": "https://api.github.com/repos/troydai/webhooktest/assignees{/user}",
    "branches_url": "https://api.github.com/repos/troydai/webhooktest/branches{/branch}",
    "tags_url": "https://api.github.com/repos/troydai/webhooktest/tags",
    "blobs_url": "https://api.github.com/repos/troydai/webhooktest/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/troydai/webhooktest/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/troydai/webhooktest/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/troydai/webhooktest/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/troydai/webhooktest/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/troydai/webhooktest/languages",
    "stargazers_url": "https://api.github.com/repos/troydai/webhooktest/stargazers",
    "contributors_url": "https://api.github.com/repos/troydai/webhooktest/contributors",
    "subscribers_url": "https://api.github.com/repos/troydai/webhooktest/subscribers",
    "subscription_url": "https://api.github.com/repos/troydai/webhooktest/subscription",
    "commits_url": "https://api.github.com/repos/troydai/webhooktest/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/troydai/webhooktest/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/troydai/webhooktest/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/troydai/webhooktest/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/troydai/webhooktest/contents/{+path}",
    "compare_url": "https://api.github.com/repos/troydai/webhooktest/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/troydai/webhooktest/merges",
    "archive_url": "https://api.github.com/repos/troydai/webhooktest/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/troydai/webhooktest/downloads",
    "issues_url": "https://api.github.com/repos/troydai/webhooktest/issues{/number}",
    "pulls_url": "https://api.github.com/repos/troydai/webhooktest/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/troydai/webhooktest/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/troydai/webhooktest/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/troydai/webhooktest/labels{/name}",
    "releases_url": "https://api.github.com/repos/troydai/webhooktest/releases{/id}",
    "deployments_url": "https://api.github.com/repos/troydai/webhooktest/deployments",
    "created_at": 1502398458,
    "updated_at": "2017-08-10T21:30:14Z",
    "pushed_at": 1502402326,
    "git_url": "git://github.com/troydai/webhooktest.git",
    "ssh_url": "git@github.com:troydai/webhooktest.git",
    "clone_url": "https://github.com/troydai/webhooktest.git",
    "svn_url": "https://github.com/troydai/webhooktest",
    "homepage": null,
    "size": 6,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 0,
    "mirror_url": null,
    "open_issues_count": 0,
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "master",
    "stargazers": 0,
    "master_branch": "master"
  },
  "pusher": {
    "name": "troydai",
    "email": "troy.dai@outlook.com"
  },
  "sender": {
    "login": "troydai",
    "id": 1329240,
    "avatar_url": "https://avatars2.githubusercontent.com/u/1329240?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/troydai",
    "html_url": "https://github.com/troydai",
    "followers_url": "https://api.github.com/users/troydai/followers",
    "following_url": "https://api.github.com/users/troydai/following{/other_user}",
    "gists_url": "https://api.github.com/users/troydai/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/troydai/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/troydai/subscriptions",
    "organizations_url": "https://api.github.com/users/troydai/orgs",
    "repos_url": "https://api.github.com/users/troydai/repos",
    "events_url": "https://api.github.com/users/troydai/events{/privacy}",
    "received_events_url": "https://api.github.com/users/troydai/received_events",
    "type": "User",
    "site_admin": false
  }
}'''

response = requests.request(
    'POST', 'http://localhost:5000/api/build',
    params={'client_id': 'build-trigger'},
    headers={'X-Hub-Signature': 'sha1=2f792568de73c7e8b131d33a81f70ddc28eaa009',
             'X-GitHub-Event': 'push'},
    data=json.dumps(json.loads(payload), indent=2))
print(response)
