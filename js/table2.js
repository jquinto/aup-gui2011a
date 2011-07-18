window.addEvent('domready', function(){
	var sum = 0;
        $('box').addEvent('click', function(){
                var count = 0;
                $('chk').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                sum = $('value1').getElements;
                        }
                });
                $('count-textbox').set('text',sum/count);
        });
                $('box2').addEvent('click', function(){
                var count = 0;
                $('chk').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('count-textbox').set('text',sum/count);
        });
                $('box3').addEvent('click', function(){
                var count = 0;
                $('chk').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('count-textbox').set('text',sum/count);
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

