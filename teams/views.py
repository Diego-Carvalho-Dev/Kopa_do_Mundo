from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Team
from django.forms.models import model_to_dict
from datetime import datetime



class TeamView(APIView):
    def post(self, request: Request):

        data = request.data

        titles = data.get("titles", 0)
        if titles < 0:
            return Response({"error": "titles cannot be negative"}, status=400)

        first_cup = data.get("first_cup")
        if first_cup:
            try:
                first_cup_date = datetime.strptime(first_cup, "%Y-%m-%d").date()
            except ValueError:
                return Response(
                    {"error": "invalid date format for first_cup"}, status=400
                )

            if first_cup_date.year < 1930:
                return Response(
                    {"error": "there was no world cup this year"}, status=400
                )

            if (first_cup_date.year - 1930) % 4 != 0:
                return Response(
                    {"error": "there was no world cup this year"}, status=400
                )

        if first_cup and titles > (datetime.now().year - first_cup_date.year + 1):
            return Response(
                {"error": "impossible to have more titles than disputed cups"},
                status=400,
            )

        new_team: Team = Team.objects.create(**data)
        return Response(model_to_dict(new_team), status=201)

    def get(self, request: Request):
        team_list = []

        for team in Team.objects.all():
            team_dict = model_to_dict(team)
            team_list.append(team_dict)

        return Response(team_list)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=404)

        return Response(model_to_dict(team))

    def patch(self, request: Request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=404)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        return Response(model_to_dict(team))

    def delete(self, request: Request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=404)

        team.delete()

        return Response(status=204)
