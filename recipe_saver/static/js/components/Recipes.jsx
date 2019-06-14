import React from "react";
import Header from "./Header"
import RecipeList from "./RecipeList"

export default class Recipes extends React.Component {
    render() {
        const params = new URLSearchParams(this.props.location.search); 
        const category = params.get('category');
        return (
            <RecipeList category={category}/>
        );
    }
}
