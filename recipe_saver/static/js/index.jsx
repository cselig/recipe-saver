import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route } from 'react-router-dom'

import Header from "./components/Header";
import App from "./components/App";
import Recipes from "./components/Recipes"
import Recipe from "./components/Recipe"

require('../css/fullstack.css');

ReactDOM.render(<Header />, document.getElementById('header'));

ReactDOM.render(
    (
        <BrowserRouter>
            <Route exact path="/" component={App}/>
            <Route path="/recipes" component={Recipes}/>
            <Route path="/recipe" component={Recipe}/>
        </BrowserRouter>
    ),
    document.getElementById('content')
);
