$(document).ready(function ()
{
    $('input,select').on('input', function ()
    {
        work(this);
    });
	
	$('input,select').each(function ()
    {
        work(this);
    });
	
	function work(el)
	{
		id = el.id + "_value";
        document.getElementById(id).innerHTML = $(el).val();

        makeRequest(
            $('#la').val(),
            $('#mu').val(),
            $('#nu').val(),
            $('#N').val(),
            $('#Nk').val(),
            $('#Np').val(),
            $('#dir').val());
	}
});

function makeRequest(la, mu, nu, N, Nk, Np, dir)
{
    $.ajax({
        method: 'GET',
        url: '/data',
        data: {
            la: la,
            mu: mu,
            nu: nu,
            N: N,
            Nk: Nk,
            Np: Np,
            dir: dir
        },
        success: function (data)
        {
            $('#N_avg').text(data.N_avg);
            $('#t_solve').text(data.solve_time);
            $('#p').empty();
            $('#p').html(data.p);
        }
    });
}