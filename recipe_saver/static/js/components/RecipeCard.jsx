import React from "react";

export default class RecipeCard extends React.Component {
    render() {
        return (
            <a href="/recipe">
                <div className="recipe-card">
                    <p>{this.props.name}</p>
                </div>
            </a>
        )
    }
}
