import React from 'react'


const TodoItem = ({todo}) => {
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
       </tr>
   )
}


const TodoList = ({todos}) => {
   return (
       <table>
           <th>
              Проект REST
           </th>
           <th>
               Имя пользователя
           </th>
           <th>
               Todo текст
           </th>
           {todos.map((todo) => <TodoItem todo={todo} />)}
       </table>
   )
}


export default TodoList