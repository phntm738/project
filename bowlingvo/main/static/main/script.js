

function LessonLogic() {
	
	var self = this;
	
	var my_button = document.getElementById('task-button');	
	
	var my_tasks = [].slice.call(document.getElementsByClassName('task'));
	
	var show_queue = [];
	
	for (var i = 0; i <= my_tasks.length; i++) {
		show_queue.push(i);
	}
	
	var score = 10;
	
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
		
		if (user_answer.toLowerCase() == answer.toLowerCase()) {
			var correct = document.getElementById('correct-answer');
			correct.hidden = false;
		} else {
			var wrong = document.getElementById('wrong-answer');
			wrong.children[0].textContent = 'Ваш ответ: ' + user_answer;
			wrong.children[1].textContent = 'Ожидаемый ответ: ' + answer;
			wrong.hidden = false;
			show_queue.push(show_queue[0]);
			score -= 1;
			if (score < 0) {
				score = 0;
			}
		}
		my_button.firstChild.data = 'Следующий';
		my_button.removeAttribute('onclick');
		my_button.setAttribute('onclick', 'lesson.getNext()');
	}
	
	self.getNext = function() {
		var reaction = document.getElementById('correct-answer');
		reaction.hidden = true;
		reaction = document.getElementById('wrong-answer');
		reaction.hidden = true;
		if (show_queue	.length > 1) {
			var cur_id = show_queue.shift();
			var next_id = show_queue[0];
			var task_old = document.getElementById('task' + cur_id);
			task_old.hidden	 = true;
			
			if (cur_id > 0){
			var user_input = task_old.getElementsByTagName('input');
			if (user_input.length == 1) {
				user_input[0].value = '';
			} else {
				for (i = 0; i < 4; i++) {
					if (user_input[i].checked) {
						user_input[i].checked = false;
					}
				}
			}
			}
			
			var task_new = document.getElementById('task' + next_id);
			task_new.hidden = false;
			var inp = task_new.getElementsByTagName('input');
			if (inp.length == 1) {
				inp[0].focus();
			}
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
			lesson_score = document.getElementById('score-input');
			lesson_score.value = score;
		}
	}		
}

document.onkeyup = function(event) {
	if (event.keyCode == 13) {
		var btn = document.getElementById('task-button');
		if (btn) {
			btn.click();
		}
	}
};

var lesson = new LessonLogic();


function GameLogic() {
	
	var self = this;
	
	var tasks = [].slice.call(document.getElementsByClassName('task'));
	
	self.check = function() {
		var url_par = document.getElementById('url_par').textContent;
		var encoded  = document.getElementById('encoded').textContent;
		var tasks = document.getElementsByClassName('task');
		var answers = [];
		for (var i = 0; i < tasks.length; i++) {
			var task = tasks[i];
			var tasktype = task.getAttribute('tasktype');
			if (task.children.length == 1) {
				var sel = task.children[0];
				var strUser = sel.options[sel.selectedIndex].value;
				answers.push([tasktype, strUser]);
			} else {
				var inp = task.children[1];
				answers.push([tasktype, inp.value]);
			}
		}
		var xhr = new XMLHttpRequest();
		xhr.open('POST', '/main/lang/' + url_par + '/game', false);
		xhr.setRequestHeader('X-CSRFToken', getCSRF());
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		xhr.send('encoded=' + encoded + '&answers=' + JSON.stringify(answers));
		var params = xhr.responseText;
		params = JSON.parse(params);
		if (params.end) {
			tasks = document.getElementById('all-tasks');
			tasks.innerHTML = '';
			tasks.hidden = true;
			document.getElementById('score').textContent = params.score;
			document.getElementById('finish-frame').hidden = false;
		} else {
			document.getElementById('encoded').textContent = params.encoded;
			for (var i = 0; i < tasks.length; i++) {
				task = tasks[i];
				task.hidden = params.ans[i];
			}
			var throw_button = document.getElementById('throw-button');
			throw_button.textContent = '2-й бросок';
		}
	}

}


var game = new GameLogic();


function show_lex() {
	lex = document.getElementById('lex-sections');
	gram = document.getElementById('gram-sections');
	document.getElementById('lex-button').classList.toggle('highlight');
	document.getElementById('gram-button').classList.toggle('highlight');
	gram.style.display = 'none';
	lex.style.display = 'block';
}


function show_gram() {
	lex = document.getElementById('lex-sections');
	gram = document.getElementById('gram-sections');
	document.getElementById('lex-button').classList.toggle('highlight');
	document.getElementById('gram-button').classList.toggle('highlight');
	lex.style.display = 'none';
	gram.style.display = 'block';
}

//----------------------tests----------------------------
function tryXHR() {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/main/test1', false);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.setRequestHeader('X-CSRFToken', getCSRF());
	xhr.send('score=10');
	
	var test = document.getElementById('test');
	test.innerHTML = xhr.responseText;
}