from views import user_view
from models.player import Player


class UserManager:
    """
    Manages the interaction between the user and the player management functionalities.

    Attributes:
        controller: The main application controller.
        user_view (user_view.UserView): The view for player-related operations.
    """

    def __init__(self, controller):
        self.controller = controller
        self.user_view = user_view.UserView(self.controller)

    def register_player(self, **kwargs) -> None:
        """Registers a new player and associates them with a tournament if one exists."""
        player = Player(**kwargs)

        # Check if a tournament exists before adding the player
        if self.controller.tournament_manager.tournament is not None:
            self.controller.tournament_manager.tournament.add_player(player)
        else:
            print("No tournament has been created. Please create a tournament before adding players.")

    def display_registration_form(self) -> None:
        """Displays the form for player registration."""
        self.user_view.display_player_form()

    def display_player_submenu(self) -> None:
        """Displays the submenu related to player operations."""
        self.user_view.display_player_submenu()

    def modify_player(self) -> None:
        """Modifies the details of a specific player. (Functionality not yet implemented)"""
        pass

    def update_player_scores(self, match) -> None:
        """Updates players' scores after a match."""
        winner = match.get_winner()
        if winner:
            self.controller.tournament_manager.tournament.add_points(winner, 1.0)
        else:  # In case of a tie
            self.controller.tournament_manager.tournament.add_points(match.player1, 0.5)
            self.controller.tournament_manager.tournament.add_points(match.player2, 0.5)
