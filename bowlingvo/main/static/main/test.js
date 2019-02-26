function hide_div(id) {
	document.getElementById(id).style.display = 'none';
}

function show_div(id) {
	document.getElementById(id).style.display = 'block';
}


function LessonLogic() {
	
	var self = this;
	
	var task_node = document.getElementById('all-tasks');
	
	var my_tasks = [].slice.call(document.getElementsByClassName('task'));
	
	var show_queue = [];
	
	for (var i = 1; i <= my_tasks.length; i++) {
		show_queue.push(i);
	}
	
	self.makeTasksList = function() {
		console.log(my_tasks);
	}
	
	self.checkTask = function() {
		var cur_id = show_queue[0];
		var task = document.getElementById('task' + cur_id);
		
		var answer = task.getAttribute('answer');
		
		var user_input = task.getElementsByTagName('input');
		
		if (user_input.length == 1) {
			var user_answer = user_input[0].value;
		} else {
			for (var inp in user_input) {
				if (inp.checked) {
					var user_answer = inp.value;
					break;
				}
			}
			if (typeof(user_answer) == "undefined") {
				var user_answer = false;
			}
		}
		
		if (user_input == answer) {
			alert('Верно');
		} else {
			alert('Неверно');
		}
	}
}


var lesson = new LessonLogic();


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
