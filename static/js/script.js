(function() {
    var $la = null;
    var $mu = null;
    var $nu = null;
    var $N = null;
    var $Nk = null;
    var $Np = null;
    var $dir = null;

    function init_input_params() {
        $la = $('#la');
        $mu = $('#mu');
        $nu = $('#nu');
        $N = $('#N');
        $Nk = $('#Nk');
        $Np = $('#Np');
        $dir = $('#dir');
    }

    $(document).ready(function ()
    {
        init_input_params();

        var $inputs = $('.param_input');
        $inputs.on('input', work);
        $inputs.each(function() {
            var $this = $(this);
            $this.slider();
            $this.on('slide', function(slideEvt) {
                work.call(this);
            });
            fill_label(this);
        });

        $('.param_input_select').on('input', function() {
            work.call(this);
        });
        makeRequest();

        //$('button')
    });

    function _makeRequest(la, mu, nu, N, Nk, Np, dir)
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

    function makeRequest() {
        _makeRequest(
            $la.val(),
            $mu.val(),
            $nu.val(),
            $N.val(),
            $Nk.val(),
            $Np.val(),
            $dir.val());
    }

    function fill_label(el) {
        var id = el.id + "_value";
        document.getElementById(id).innerHTML = $(el).val();
    }

    function work()
    {
        fill_label(this);
        makeRequest();
    }
})();