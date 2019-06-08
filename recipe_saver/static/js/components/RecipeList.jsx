import React from "react";
import RecipeCard from "./RecipeCard"

var $ = require("jquery");

export default class RecipeList extends React.Component {
    constructor(props) {
        super(props);

        console.log(props)

        this.state = {recipe_arr: []};
    }

    componentDidMount() {
        this.getRecipes();
    }

    getRecipes() {
        console.log(this.props);
        return $.getJSON("/get_recipes?category=" + this.props.category, (data) => {
            console.log(data);
            this.setState({recipe_arr: data});
        });
    }

    render() {
        return (
            <div className="recipe-list">
                {this.state.recipe_arr.map((value, index) => {
                    return <RecipeCard name={value} key={index} />
                })}               
            </div>
        );
    }
}
