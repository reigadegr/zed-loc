    # 检查是否为纯数字
    if key.isdigit():
        return True

    # 检查是否为纯标点符号
    if re.match(r'^[^\w\s]+$', key):
        return True

