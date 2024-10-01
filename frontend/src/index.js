import React from 'react';
import ReactDOM from 'react-dom/client';
import { Router, Switch, Route } from 'react-router-dom';
import history from './history';
import './index.css';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransaction from './components/ConductTransactions';
import TransactionPool from './components/TransactionPool';

// ReactDOM.render(<App />, document.getElementById('root'));

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router history={history}>
    <Switch>
      <Route path='/' exact component={App} />
      <Route path='/blockchain' component={Blockchain} />
      <Route path='/conduct-transaction' component={ConductTransaction} />
      <Route path='/transaction-pool' component={TransactionPool} />
    </Switch>
  </Router>
);

// ReactDOM.render(
//   <Router history={createBrowserHistory()}>
//     <Switch>
//       <Route path='/' exact component={App} />
//       <Route path='/blockchain' component={Blockchain} />
//       <Route path='/conduct-transaction' component={ConductTransaction} />
//     </Switch>
//   </Router>,
//   document.getElementById('root')
// );