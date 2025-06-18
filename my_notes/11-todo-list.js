const todoList = ['make dinner', 'wash dishes'];

renderTodoList();

function renderTodoList() {

let todoListHTML = '';

// This Technique is called generating HTML
for (let i = 0; i < todoList.length; i++) {
  const todo = todoList[i];
  const html = `
    <p>
      ${todo}
      <button onclick="
        todoList.splice(${i}, 1);
        renderTodoList();
      ">Delete</button>
    </p>
  `;
  todoListHTML += html;
}

document.querySelector('.js-todo-list')
  .innerHTML = todoListHTML;

}

function addTodo() {
  const inputElement = document.querySelector('.js-name-input');
  const name = inputElement.value 

  todoList.push(name);
  console.log(todoList);
  inputElement.value = '';

  renderTodoList();

  // This resets the search bar to make it empty, remember you will still see the placeholder text regardless. Pretty handy!
}