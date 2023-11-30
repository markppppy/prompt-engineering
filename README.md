[toc]

# prompt-engineering
- 项目分四个部分
  - 面向开发者的提示工程
    - 是什么：针对特定任务构造能充分发挥大模型能力的prompt的技巧，介绍如何构造 Prompt 并基于 OpenAI 提供的 API 实现包括总结、推断、转换等多种常用功能，并基于上述技巧实现个性化定制功能。
    - 为什么：随着 ChatGPT 等 LLM（大语言模型）的出现，自然语言处理的范式正在由 Pretrain-Finetune（预训练-微调）向 Prompt Engineering（提示工程）演变。对于具有较强自然语言理解、生成能力，能够实现多样化任务处理的 LLM 来说，一个合理的 Prompt 设计极大地决定了其能力的上限与下限。
    - 怎么做：书写 Prompt 的原则与技巧；文本总结（如总结用户评论）；文本推断（如情感分类、主题提取）；文本转换（如翻译、自动纠错）；扩展（如书写邮件）等。
  - 搭建基于 ChatGPT 的问答系统
  - 使用 LangChain 开发应用程序
  - 使用 LangChain 访问个人数据 
- 参考吴恩达等人的[面向开发者的LLM入门教程](https://datawhalechina.github.io/prompt-engineering-for-developers/#/C1/readme)
## 面向开发者的提示工程 
- 开发目的：大语言模型（LLM） 的更强大功能是能通过 API 接口调用，从而快速构建软件应用程序
- LLM分类：基础LLM 和 指令微调（Instruction Tuned）LLM
  - 基础LLM是基于文本训练数据，训练出预测下一个单词能力的模型(todo:不是回答问题吗)
  - 指令微调LLM是基于预训练的语言模型，通过专门的训练，使其更好地理解并遵循指令；有时也会采用RLHF（reinforcement learning from human feedback，人类反馈强化学习）技术，根据人类对模型输出的反馈进一步增强模型遵循指令的能力。指令微调 LLM 可以生成对指令高度敏感、更安全可靠的输出，较少无关和损害性内容。
- prompt的设计原则
  - 编写清晰、具体的指令
    - 使用分隔符清晰地表示输入的不同部分，可以使用````，"""，< >，<tag> </tag>，:`等作为分隔符，例如：
      ```python
      from tool import get_completion
  
      text = f"""
      您应该提供尽可能清晰、具体的指示，以表达您希望模型执行的任务。
      这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性...
      """
      # 需要总结的文本内容
      prompt = f"""
      把三个单引号括起来的文本总结成一句话。
      '''{text}'''
      """
  
      # 指令内容，使用 ``` 来分隔指令和待总结的内容
      response = get_completion(prompt)
      print(response)
      ```
    - 结构化输出
      ```python
      prompt = f"""
      请生成包括书名、作者和类别的三本虚构的、非真实存在的中文书籍清单，\
      并以 JSON 格式提供，其中包含以下键:book_id、title、author、genre。
      """
      ```
    - 要求模型检查是否满足条件
      ```python
      prompt = f"""
      ...(省略)
      如果文本中不包含一系列的指令，则直接写“未提供步骤”。
      """
      ```
    - 提供少量示例
      ```python
      prompt = f"""
      您的任务是以一致的风格回答问题。(明确任务)
      <孩子>: 请教我何为耐心。
      <祖父母>: 挖出最深峡谷的河流源于一处不起眼的泉眼；最宏伟的交响乐从单一的音符开始；最复杂的挂毯以一根孤独的线开始编织。
      <孩子>: 请教我何为韧性。
      """
      ```
  - 给模型时间思考：通过前置多个问题引导想要的答案
    - 指定完成任务所需的步骤和回答格式
    - 指导模型在下结论之前找出一个自己的解法，然后通过和已有的答案对比是否一致，来判断已有的答案是否正确
  - 局限：模型没有完全记住所见的信息，难以判断自己的知识边界，可能做出错误的推断，产生一些看似真实，实则编造的知识，这个现象叫做幻觉。目前开发者只能通过prompt的设计尽量避免此类问题，如让模型先引用原文等。
- prompt的迭代优化
  