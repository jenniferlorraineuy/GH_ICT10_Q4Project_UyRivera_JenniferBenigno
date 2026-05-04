from pyscript import document
import numpy as np
import io
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

attendance_data = {
    'Monday':    None,
    'Tuesday':   None,
    'Wednesday': None,
    'Thursday':  None,
    'Friday':    None,
}

def count_logged():
    return sum(1 for v in attendance_data.values() if v is not None)

def update_stats():
    values = [v for v in attendance_data.values() if v is not None]
    total  = sum(values) if values else 0
    logged = count_logged()
    avg    = round(total / logged, 1) if logged > 0 else '—'
    peak   = max(values) if values else '—'

    document.getElementById('stat-total').textContent  = str(total)
    document.getElementById('stat-logged').textContent = str(logged)
    document.getElementById('stat-avg').textContent    = str(avg)
    document.getElementById('stat-peak').textContent   = str(peak)

def update_table():
    tbody = document.getElementById('summary-body')
    tbody.innerHTML = ''

    for day in days_of_week:
        value = attendance_data[day]
        row   = document.createElement('tr')

        day_cell = document.createElement('td')
        day_cell.textContent = day

        abs_cell = document.createElement('td')
        badge    = document.createElement('td')

        if value is not None:
            abs_cell.textContent = str(value)
            abs_cell.className   = 'logged'
            badge.innerHTML      = '<span class="badge-logged">Logged</span>'
        else:
            abs_cell.textContent = '—'
            abs_cell.className   = 'not-logged'
            badge.innerHTML      = '<span class="badge-not-logged">Pending</span>'

        row.appendChild(day_cell)
        row.appendChild(abs_cell)
        row.appendChild(badge)
        tbody.appendChild(row)

def update_progress():
    logged  = count_logged()
    percent = (logged / 5) * 100
    document.getElementById('progress-bar').style.width   = f'{percent}%'
    document.getElementById('progress-label').textContent = f'{logged} / 5 days logged'

def log_absence(event):
    selected_day  = document.getElementById('day-select').value
    absence_value = document.getElementById('absence-input').value
    status        = document.getElementById('status-message')

    if absence_value == '' or absence_value is None:
        status.innerHTML  = 'Please enter a number.'
        status.className  = 'status status-error'
        return

    absence_count = int(absence_value)

    if absence_count < 0:
        status.innerHTML = 'Cannot be negative.'
        status.className = 'status status-error'
        return

    attendance_data[selected_day] = absence_count
    status.innerHTML = f'{selected_day}: {absence_count} absence(s) saved.'
    status.className = 'status status-success'
    document.getElementById('absence-input').value = ''

    update_table()
    update_progress()
    update_stats()

def show_graph(event):
    absence_values = np.array([
        attendance_data[day] if attendance_data[day] is not None else 0
        for day in days_of_week
    ])
    day_labels = np.array(days_of_week)

    fig, ax = plt.subplots(figsize=(8, 3.8))
    fig.patch.set_facecolor('#f6f9f4')
    ax.set_facecolor('#ffffff')

    ax.plot(day_labels, absence_values,
            color='#5a8a5a', marker='o', linewidth=2,
            markersize=8, markerfacecolor='#ffffff',
            markeredgecolor='#5a8a5a', markeredgewidth=2)

    ax.fill_between(day_labels, absence_values,
                    alpha=0.15, color='#5a8a5a')

    ax.set_xlabel('Day', color='#7a8a7a', fontsize=9)
    ax.set_ylabel('Absences', color='#7a8a7a', fontsize=9)
    ax.tick_params(colors='#7a8a7a', labelsize=8)

    for spine in ax.spines.values():
        spine.set_edgecolor('#e4ede0')

    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.grid(axis='y', color='#e4ede0', linestyle='--', linewidth=0.7)

    plt.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='svg', bbox_inches='tight')
    buf.seek(0)
    svg_data = buf.read().decode('utf-8')
    plt.close(fig)

    graph_output = document.getElementById('graph-output')
    graph_output.innerHTML = svg_data

update_table()
update_progress()
update_stats()
