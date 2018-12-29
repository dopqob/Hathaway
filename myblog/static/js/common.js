function reply(comment_name, comment_id) {
    $('#content').attr('placeholder', '回复' + comment_name + '的内容：'); // 设置内容输入框的提示
    $('#reply').val(comment_id) //设置隐藏元素的值为评论目标的id
}