function hide_div(id) {
	document.getElementById(id).style.display = 'none';
}

function show_div(id) {
	document.getElementById(id).style.display = 'block';
}


function LessonLogic() {
	
	var self = this;
	
	var my_button = document.getElementById('task-button');
	
	var my_tasks = [].slice.call(document.getElementsByClassName('task'));
	
	var show_queue = [];
	
	for (var i = 0; i <= my_tasks.length; i++) {
		show_queue.push(i);
	}
	
	var score = 0;
	
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
			var user_answer = '';
			for (i = 0; i < 4; i++) {
				if (user_input[i].checked) {
					user_answer = user_input[i].value;
				}
			}
		}
		
		if (user_answer == answer) {
			alert('Верно');
			score += 10;
		} else {
			alert('Неверно');
			show_queue.push(show_queue[0]);
			score -= 5;
			if (score < 0) {
				score = 0;
			}
		}
		my_button.firstChild.data = 'Следующий';
		my_button.removeAttribute('onclick');
		my_button.setAttribute('onclick', 'lesson.getNext()');
	}
	
	self.getNext = function() {
		if (show_queue.length > 1) {
			var cur_id = show_queue.shift();
			var next_id = show_queue[0];
			var task_old = document.getElementById('task' + cur_id);
			task_old.hidden	 = true;
			var task_new = document.getElementById('task' + next_id);
			task_new.hidden = false;
			my_button.firstChild.data = 'Проверить';
			my_button.removeAttribute('onclick');
			my_button.setAttribute('onclick', 'lesson.checkTask()');
		} else {
			var task = document.getElementById('task' + show_queue.shift());
			var end = document.getElementById('finish');
			task.parentNode.hidden = true;
			end.hidden = false;
			var lesson_score = document.getElementById('lesson-score');
			lesson_score.textContent = score;
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
