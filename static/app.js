class ActivateEvents {
    constructor() {
        this.activateButtons();
        this.score = 0;
        this.startingTime = 60;
        setInterval(() => {
            if (this.startingTime > 0) {
                this.startingTime -= 1;
                $("#timer").text(this.startingTime);
                if (this.startingTime < 6) {
                    $('#timer').addClass('urgent')
                };
            }
        }, 1000);

        setTimeout(async () => {
            $("#timer").text("TIMES UP!");
            $('#score-title').text("FINAL SCORE: ")
            const response = await axios.get(`http://127.0.0.1:5000/submit-score/${$('#score').text()}`);
            $('#top-score').text(response.data.top_score);
            $('#attempts').text(response.data.attempts);
            $('.guess-input').hide();
            $('#restart').show();
        }, 60000);
    }

    activateButtons() {
        $('#submit-button').on("click", this.guessNotification.bind(this));
    }

    scoreKeeper(res) {
        if (res.result == "valid word!") {
            this.score += res.word.length;
            $('#score').text(this.score)
        }
    }

    async guessNotification(event) {
        event.preventDefault();
        $('.temp-notify').remove();
        const resultObj = await this.guessResult();
        $('.notification').append(`<div class="temp-notify">"${resultObj.word}" - ${resultObj.result}</div>`)
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
let newGame;
$('#restart').hide()
$('.container').hide()

$('#start-game').on("click", function () {
    $('.container').slideDown();
    newGame = new ActivateEvents;
    $('#start-game').hide();
})





