class ActivateEvents {
    constructor() {
        this.activateSubmitBtn();
        this.score = 0;
    }

    activateSubmitBtn() {
        $('button').on("click", this.guessNotification.bind(this));
    }

    scoreKeeper(res) {
        if(res.result=="valid word!"){
            this.score += res.word.length;
            $('#score').text(this.score)
        }
    }

    async guessNotification(event) {
        event.preventDefault();
        $('.temp-notify').remove();
        const resultObj = await this.guessResult();
        $('.notification').append(`<div class="temp-notify">${resultObj.word} : ${resultObj.result}</div>`)
        $('.temp-notify').delay(1000).fadeOut(500)
        $('#guess').val("");
    }

    async guessResult(event) {
        const guess = $('#guess').val();
        const response = await axios.get(`http://127.0.0.1:5000/${guess}`);
        this.scoreKeeper(response.data);
        return response.data;
    }
}



