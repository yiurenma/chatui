var bot = new ChatSDK({
    config: {
        robot: {
            avatar: '//gw.alicdn.com/tfs/TB1U7FBiAT2gK0jSZPcXXcKkpXa-108-108.jpg'
        },
        messages: [
            {
                type: 'text',
                content: {
                    text: '您好，小爱为您服务，请问有什么可以帮您的？'
                }
            }
        ],
        placeholder: '输入任何您想询问的问题',
    },
    requests: {
        send: function (msg) {
            if (msg.type === 'text') {
                return {
                    url: 'https://3ofgbb30ne.execute-api.us-east-1.amazonaws.com/dev/chat',
                    data: {
                        text: msg.content.text
                    },
                    headers: {
                        'ngrok-skip-browser-warning': 'skip'
                    }
                };
            }
        }
    },
    handlers: {
        parseResponse: function (res, requestType) {
            if (requestType === 'send' && res.choices) {
                return [{"_id":res.data,type:"text",content:{text:res.choices[0].message.content},position:"left"}];
            }
        },
    },
});
bot.run();