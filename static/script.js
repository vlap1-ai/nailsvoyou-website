flatpickr("#appointment-date", {
    dateFormat: "F j, Y",
    minDate: "today"
});

flatpickr("#appointment-time", {
    enableTime: true,
    noCalendar: true,
    dateFormat: "h:i K",
    time_24hr: false
});