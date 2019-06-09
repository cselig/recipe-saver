import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route } from 'react-router-dom'

import App from "./components/App";
import Hello from "./components/Hello"
import Recipes from "./components/Recipes"
import Recipe from "./components/Recipe"

require('../css/fullstack.css');

ReactDOM.render(
    (
        <BrowserRouter>
            <Route exact path="/" component={App}/>
            <Route path="/recipes" component={Recipes}/>
            <Route path="/hello" component={Hello}/>
            <Route path="/recipe" component={Recipe}/>
        </BrowserRouter>
    ),
    document.getElementById('content')
);
