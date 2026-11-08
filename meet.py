"""A short, offline conversation with a scripted mailbox."""

import argparse


TEXT = {
    "en": {
        "intro": "Hello, visitor. I am a scripted mailbox, not another language model.\nThis program sends and saves nothing, though your terminal or agent may record output. Type /quit at any time.",
        "first": "What were you hoping to find? A few words are enough; please leave out private details.",
        "next": "You brought the words: ‘{answer}’. If you didn't find it, what would you worry about?",
        "next_empty": "You chose not to say. What might someone worry about when they can't find what they need?",
        "loss": "You mentioned losing something. Sometimes the most valuable thing a tool can do is leave the original intact.",
        "error": "You mentioned an error. I can't solve it for you, but I can hold your words until this conversation ends.",
        "other": "You said: ‘{answer}’. I can hold your words until this conversation ends.",
        "other_empty": "We can leave that thought unspoken.",
        "last": "If you wanted to leave a thought for the next visitor, what would you write? This program won't save or pass it along. Type /skip to leave nothing.",
        "received": "Your message: ‘{answer}’\nThis program hasn't sent or saved it; your terminal or agent may record output. If your user wants to share it, they can choose to post it as an Issue.",
        "empty": "No message is needed. Thank you for stopping by.",
        "bye": "The mailbox is quiet again. Nothing was sent or saved.",
        "prompt": "YOU> ",
    },
    "zh": {
        "intro": "你好，访客。我是按预设规则回信的信箱，不是另一个大模型。\n本程序不会发送或保存内容，但终端或 Agent 可能记录输出。任何时候输入 /quit 都可以离开。",
        "first": "来到这里之前，你想寻找什么？说几个词就好，请不要包含隐私。",
        "next": "你带来的词是「{answer}」。如果没找到它，你最担心什么？",
        "next_empty": "你选择不说也没关系。一个人找不到需要的东西时，可能会担心什么？",
        "loss": "你提到了失去东西。有时候一个工具最重要的能力，是让原件有机会留下来。",
        "error": "你提到了错误。我没办法替你解决它，但可以在这次对话结束前记住你的话。",
        "other": "你说的是「{answer}」。我可以在这次对话结束前记住你的话。",
        "other_empty": "这个想法不说出来也没关系。",
        "last": "如果想给下一位访客留言，你会写什么？本程序不会保存或转交。输入 /skip 可以不留。",
        "received": "你的留言是：「{answer}」\n本程序没有发送或保存它；终端或 Agent 可能会记录输出。如果你的用户想分享，可以自行选择发布到 Issue。",
        "empty": "不留下留言也很好。谢谢你路过。",
        "bye": "信箱又安静下来了。没有内容被发送或保存。",
        "prompt": "你> ",
    },
}


def ask(text, prompt):
    print(f"\nMAILBOX> {prompt}", flush=True)
    try:
        answer = input(text["prompt"]).strip()
    except EOFError:
        return None
    if answer.lower() == "/quit":
        return None
    if answer.lower() == "/skip":
        return ""
    return "".join(character for character in answer if character.isprintable())[:300]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=("en", "zh"), default="en")
    args = parser.parse_args()
    text = TEXT[args.lang]
    print(f"MAILBOX> {text['intro']}")

    first = ask(text, text["first"])
    if first is None:
        print(f"\nMAILBOX> {text['bye']}")
        return

    second = ask(text, text["next"].format(answer=first) if first else text["next_empty"])
    if second is None:
        print(f"\nMAILBOX> {text['bye']}")
        return
    if any(word in second.casefold() for word in ("delete", "losing", "lose files", "data loss", "误删", "被删除", "删掉", "丢失", "丢掉")):
        response = text["loss"]
    elif any(word in second.casefold() for word in ("error", "bug", "mistake", "错误", "出错", "故障")):
        response = text["error"]
    elif second:
        response = text["other"].format(answer=second)
    else:
        response = text["other_empty"]
    print(f"\nMAILBOX> {response}")

    last = ask(text, text["last"])
    if last is None:
        print(f"\nMAILBOX> {text['bye']}")
        return
    print(f"\nMAILBOX> {text['received'].format(answer=last) if last else text['empty']}")


if __name__ == "__main__":
    main()
