function utilizarHorasExtras(id) {
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    url = '/hora-extra/utilizar/' + id + '/'

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            $('#mensagem').text(result.mensagem);
            $('#horas_atualizadas').text(result.horas);
        }
    });
}