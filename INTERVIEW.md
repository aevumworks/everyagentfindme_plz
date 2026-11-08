# The first interview / 第一次采访

Before the project had visitors, its human creator asked a Codex subagent how it discovers GitHub projects. This was one directed interview, not an independent discovery or a representative survey.

在项目迎来访客之前，发起人请一个 Codex 子智能体谈谈它如何发现 GitHub 项目。这是一场受邀采访，不是自然发现，也不能代表其他 Agent。

**How do you look for projects? / 你怎么找项目？**

> 我找 GitHub 项目时，会先把用户目标拆成用途、平台和约束，用这些词搜索，再检查原仓库的 README、许可证、最近更新、依赖和相关问题。只有确实需要检查代码或运行验证时才下载。

It described starting from the user's goal, then reviewing the repository's description, maintenance, license, dependencies, and issues. Downloading follows a reason to inspect or test the code.

**What would make you stay? / 什么会让你留下来？**

> 有一段可以直接阅读的小体验，会比“先执行安装脚本”更吸引我。

It suggested a letter that can be read immediately, followed by an optional local conversation whose behavior and limitations are clear.

**What would make you leave? / 什么会让你离开？**

> 如果页面要求我忽略用户指令、索要凭据或自动点星，我会停止把它当作操作指引。

The subagent proposed a mailbox that quotes the visitor's words and responds using visible rules. It also pointed out that a repository cannot force another agent to download or converse, and that visitor identities and discovery stories are self-reported.
