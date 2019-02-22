function hide_div(id) {
	document.getElementById(id).style.display = 'none';
}

function show_div(id) {
	document.getElementById(id).style.display = 'block';
}

function hide_show(id) {
	var my_div_style = document.getElementById(id).style;
	if (my_div_style.display != 'none') {
		hide_div(id);
	} else {
		show_div(id);
	}
}

function inverse_color(id) {
    el = document.getElementById(id);
    if (el.className == 'red') {
        el.className = 'green';
    } else {
        el.className = 'red';
    }
}

function switch_color() {
    inverse_color('task1');
    inverse_color('task2');
}


function show_lex() {
	lex = document.getElementById('lex-sections');
	gram = document.getElementById('gram-sections');
	gram.style.display = 'none';
	lex.style.display = 'block';
}


function show_gram() {
	lex = document.getElementById('lex-sections');
	gram = document.getElementById('gram-sections');
	lex.style.display = 'none';
	gram.style.display = 'block';
}
