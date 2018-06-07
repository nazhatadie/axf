function addShop(goods_id) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/market/addshop/',
        type: 'post',
        data: {'goods_id': goods_id},
        dataType: 'json',
        headers: {'X-CSRFToKen': csrf},
        success: function (msg) {
            $("#num_" + msg.goods_id).html(msg.c_num);
            $("#allgoods_sum").html('总价:' + msg.sum + '元');
            },
        error: function (msg) {
            alert('失败')
        }
    })
}


function subShop(goods_id) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/market/subshop/',
        type: 'post',
        data: {'goods_id': goods_id},
        dataType: 'json',
        headers: {'X-CSRFToKen': csrf},
        success: function (msg) {
            $("#num_" + msg.goods_id).html(msg.c_num)
            $("#allgoods_sum").html('总价:' + msg.sum + '元');
            },
        error: function (msg) {
            alert('失败')

        }

    })


}

function select_shop(cart_id) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val()

    $.ajax({
        url: '/cart/select_shop/',
        type: 'post',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if (msg.all_select) {
                a = '<span onclick="select_all(1)">√</span>';
            } else {
                a = '<span onclick="select_all(0)">x</span>';
            }
            if (msg.is_select) {
                s = ' <span onclick="select_shop(' + cart_id + ')">√</span>';
            }
            else {
                s = ' <span onclick="select_shop(' + cart_id + ')">x</span>';
            }

            $('#num_' + cart_id).html(s)
            $('#selectAll').html(a)
            $("#allgoods_sum").html('总价:' + msg.sum + '元');

        },
        error: function (msg) {
            alert('失败')

        }
    })

}

// function select_all(is_select) {
//     csrf = $('input[name="csrfmiddlewaretoken"]').val()
//
//     $.ajax({
//         url: '/cart/select_all/',
//         type: 'post',
//         data: {'is_select': is_select},
//         dataType: 'json',
//         headers: {'X-CSRFToken': csrf},
//         success: function(msg){
//             alert(msg.is_select)
//             if (msg.is_select) {
//                 s = ' <span onclick="select_shop(1)">√</span>';
//             }else {
//                 s = ' <span onclick="select_shop(0)">x</span>';
//             }
//             for (var i = 0; i < msg.cart_id.length; i++) {
//                 if (msg.is_select) {
//                     a = ' <span onclick="select_shop(' + msg.cart_id[i]+')">√</span>';
//                     console.log(msg.cart_id[i])
//                 }
//                 else {
//                     a = ' <span onclick="select_shop('+ msg.cart_id[i]+')">x</span>';
//                 }
//                 $('#num_' + msg.cart_id[i]).html(a)
//             }
//             $('#selectAll').html(s)
//         },
//         error: function (msg) {
//             alert('失败')
//         }
//     })
//
// }
function select_all(select) {
    csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/cart/select_all/',
        type: 'POST',
        data: {'select': select},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if (msg.select) {
                s = '<span onclick="select_all(1)">√</span>';
            } else {
                s = '<span onclick="select_all(0)">x</span>';
            }
            for (var i = 0; i < msg.cart_id.length; i++) {
                if (msg.select) {
                    a = '<span onclick="select_shop(' + msg.cart_id[i] + ')">√</span>';
                } else {
                    a = '<span onclick="select_shop(' + msg.cart_id[i] + ')">x</span>';
                }
                $('#num_' + msg.cart_id[i]).html(a)
            }
            $('#selectAll').html(s)
            $("#allgoods_sum").html('总价:' + msg.sum + '元');

        },
        error: function (msg) {
            alert('失败')
        }
    })
}