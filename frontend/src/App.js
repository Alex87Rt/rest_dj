import React from 'react'
import axios from 'axios'
// import logo from './logo.svg';
import './App.css'
import UserList from './components/Users.js'
import TodoList from './components/Todos.js'
import ProjectList from './components/Projects.js'
import {HashRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

const NotFound404 = ({ location }) => {
    return (
      <div>
          <h1>Страница по адресу '{location.pathname}' не найдена</h1>
      </div>
    )
  }


class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos':[]
       }
   }

   componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/')
        .then(response => {
            const users = response.data.results
                this.setState(
                {
                    'users': users
                }
            )
        }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/todos/')
        .then(response => {
            const todos = response.data.results
                this.setState(
                {
                    'todos': todos
                }
            )
        }).catch(error => console.log(error))
    
    axios.get('http://127.0.0.1:8000/api/projects/')
        .then(response => {
            const projects = response.data.results
                this.setState(
                {
                    'projects': projects
                }
            )
        }).catch(error => console.log(error))
   }    

    render() {
        return (
            <div>
              <HashRouter>
              <nav>
                <ul>
                  <li>
                    <Link to='/'>Пользователи</Link>
                  </li>
                  <li>
                    <Link to='/todos'>Todos</Link>
                  </li>
                  <li>
                    <Link to='/projects'>Проекты</Link>
                  </li>
                </ul>
              </nav>
                <Switch>
                  <Route exact path='/' component={() => <UserList users={this.state.users} />}  />
                  <Route exact path='/todos' component={() => <TodoList todos={this.state.todos} />} />
                  <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />              
                  <Redirect from='/users' to='/' />    
                  <Route component={NotFound404} />
                </Switch>
              </HashRouter>
            </div>
        )
      }
}

export default App;
