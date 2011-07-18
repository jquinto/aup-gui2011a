window.addEvent('domready', function(){
        $('box').addEvent('click', function(){
                var count = 0;
                $('chk').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('count-textbox').set('text',count);
        });
                $('box2').addEvent('click', function(){
                var count = 0;
                $('chk').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('count-textbox').set('text',count);
        });
                $('box3').addEvent('click', function(){
                var count = 0;
                $('chk').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('count-textbox').set('text',count);
        });
                $('box4').addEvent('click', function(){
                var count = 0;
                $('chk').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('count-textbox').set('text',count);
        });
});

