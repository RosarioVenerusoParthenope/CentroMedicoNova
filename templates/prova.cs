<div class="list-group">
        <a href="{% url 'visualizza_prenotazioni' %}" class="list-group-item list-group-item-action">
            📅 Le mie prenotazioni
        </a>

        <a href="{% url 'visualizza_referti' %}" class="list-group-item list-group-item-action">
            📝 Referti disponibili
        </a>
        <a href="{% url 'visualizza_fatture' %}" class="list-group-item list-group-item-action">
            💳 Le mie fatture
        </a>
        <a href="{% url 'logout' %}" class="list-group-item list-group-item-action text-danger">
            🔓 Logout
        </a>
    </div>