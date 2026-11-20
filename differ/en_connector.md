---
title: How to Use the SpeedyIndex Claude MCP connector in Claude
seo_title: Using the SpeedyIndex Claude MCP connector in Claude
meta_description: Connect SpeedyIndex to Claude with the Claude MCP connector: add the remote server, sign in, check balance, index checks, indexing, backlinks, rank tracking.
keyword: claude mcp connector (70/KD19 (us))
tags: SEO, Artificial Intelligence, Marketing
cover: /home/claude/differ/en_connector_cover.png
video: RTmBI8AV2lw
---

# How to Use the SpeedyIndex Claude MCP connector in Claude

The SpeedyIndex Claude MCP connector lets you control SpeedyIndex tools directly from a Claude chat: check your balance, run Google and Yandex indexing tasks, verify index status on Google, Yandex, and Bing, check live backlinks, and track Google rankings. You add the remote server `mcp.speedyindex.com/mcp` as a custom connector in Claude, sign in with your SpeedyIndex API key, and enable the connector in the chat. After that, you can ask Claude to run read-only checks or start paid tasks with your approval.

The connector itself is free to add; paid actions spend SpeedyIndex tokens, and new accounts include 100 tokens. The full steps for adding the server are covered in the [SpeedyIndex MCP connector setup guide](https://en.speedyindex.com/mcp/), and a short video shows the connection flow.

![SpeedyIndex + Claude — video](https://img.youtube.com/vi/RTmBI8AV2lw/hqdefault.jpg)

## What the SpeedyIndex Claude MCP connector Does

SpeedyIndex runs the MCP server remotely over Streamable HTTP. The remote server exposes 22 tools: 15 tools only read data and are free, and 7 tools change the account and ask for confirmation unless you set them to Always allow. Of those 7, five spend tokens or credits: `create_indexing_task`, `submit_single_url`, `create_index_check_task`, `create_backlink_check_task`, and `rank_tracker_start_check`. Creating a Rank Tracker project and adding keywords is free; running a check is not, and the check cost is shown in advance with `rank_tracker_get_check_cost`.

Read-only tools include:
- `get_balance`
- `list_tasks`
- `get_task_status`
- `get_task_report`
- `get_backlink_check_status`
- `get_backlink_check_report`
- `rank_tracker_get_positions`
- `rank_tracker_get_trend`
- `rank_tracker_get_keyword_details`
- `rank_tracker_list_projects`

## Connecting SpeedyIndex to Claude

In Claude on the web or desktop, open Plugins (formerly Customize → Connectors), choose Add custom connector, name it SpeedyIndex, and enter `mcp.speedyindex.com/mcp` as the URL. After Continue and Connect, a SpeedyIndex sign-in page opens; paste the API key from the API section of your SpeedyIndex account. The key is not typed into the chat. Then in a chat, click the plus sign in the message box, open Connectors, and turn SpeedyIndex on. A quick test is to ask: “What is my SpeedyIndex balance?” If Claude returns tokens and credits, the connection works.

Custom connectors work on every Claude plan, but the Free plan allows one custom connector. On Team/Enterprise plans, an Owner adds the connector in Organization settings → Connectors, and each member then connects individually. Custom connectors are not verified by Anthropic, so connect only servers you trust.

## Tool Permissions and Security

Claude asks for approval before tool calls; you can set trusted tools to Always allow. SpeedyIndex's 7 account-changing tools — including the 5 that spend tokens — ask for confirmation unless set to Always allow. The 15 read-only tools do not spend anything. The server does not keep a database; your API key is stored only inside an encrypted token. The access token lives for one hour, and sign-in renews for up to 90 days. Changing the key in your SpeedyIndex account revokes all sign-ins. The connector cannot pay, create invoices, delete projects, or delete tasks.

## Index Checks, Indexing, Backlinks, and Rank Tracking

You can check whether pages are in Google's index with the [bulk Google index checker](https://en.speedyindex.com/google-index-checker/), which handles up to 10,000 URLs per task and returns indexed and not-indexed lists with page titles for Google. SpeedyIndex also checks Yandex and Bing. For indexing, you can create Google or Yandex tasks with up to 10,000 URLs each; Google tasks are pay-per-indexed, so tokens for URLs that do not get indexed return automatically. You can spread a Google task over 2–30 days with drip feed. The backlink checker opens donor pages you provide and verifies that they still link to your domains, reporting HTTP status, anchor text, nofollow flag, and Moz Domain Authority and spam score per donor, for up to 50 target domains. Rank Tracker covers Google desktop, with projects that support up to 5 regions and 10 competitors, showing positions, changes since the last check, trend history up to 90 checks, and whether Google's AI Overview appears and cites your site.

## FAQ

### How do you connect SpeedyIndex to Claude?

Add the remote server `mcp.speedyindex.com/mcp` as a custom connector in Claude, sign in with your SpeedyIndex API key, and activate the connector in the chat using the plus sign → Connectors. The Free plan allows one custom connector; Team/Enterprise owners add it in Organization settings first. The connector itself is free, but paid tasks spend SpeedyIndex tokens.

### Does the Claude MCP connector ask before running tasks?

Yes. Claude asks for approval before tool calls, and SpeedyIndex's 7 account-changing tools — including the 5 that spend tokens — ask for confirmation unless you set them to Always allow. The 15 read-only tools are free and do not spend anything.

### What can you do after connecting the Claude MCP connector?

You can check your balance, create Google and Yandex indexing tasks, run Google, Yandex, and Bing index checks, verify live backlinks on donor pages, and track Google rankings with AI Overview presence and citation data.