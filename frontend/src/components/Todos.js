import React from 'react'


const TodoItem = ({todo, deleteTodo}) => {
   return (
       <tr>
           <td>
               {todo.project.title}
           </td>
           <td>
               {todo.user.username}
           </td>
           <td>
               {todo.text}
           </td>
           <td><button type='button' onClick={() => deleteTodo(todo.id)}>Delete</button></td>
       </tr>
   )
}


const TodoList = ({todos, deleteTodo}) => {
   return (
       <table>
           <th>
                Наименование проекта
           </th>
           <th>
                Пользователь
           </th>
           <th>
               Todo Text
           </th>
           {todos.map((todo) => <TodoItem todo={todo} deleteTodo={(id) => deleteTodo(id)}/>)}
       </table>
   )
}


export default TodoList