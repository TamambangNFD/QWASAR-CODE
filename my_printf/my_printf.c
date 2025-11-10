#include <stdarg.h>
#include <unistd.h>
#include <stdlib.h>


int my_putchar(char c)
{
    write(1, &c, 1);
    return 1;
}

int my_putstr(const char *s)
{
    int count = 0;

    if (!s)
        s = "(null)";
    while (*s) {
        write(1, s++, 1);
        count++;
    }
    return count;
}


int my_putnbr_base(unsigned long n, const char *base)
{
    unsigned long base_len = 0;
    int count = 0;

    while (base[base_len])
        base_len++;

    if (n >= base_len)
        count += my_putnbr_base(n / base_len, base);
    count += my_putchar(base[n % base_len]);

    return count;
}

int my_putnbr(long n)
{
    int count = 0;
    unsigned long un;

    if (n < 0) {
        count += my_putchar('-');
        un = (unsigned long)(-(n + 1)) + 1;
    } else {
        un = (unsigned long)n;
    }

    count += 0; 
    return count + my_putnbr_base(un, "0123456789");
}


static int handle_format(char spec, va_list *args)
{
    int count = 0;

    if (spec == 'd' || spec == 'i') {
        count += my_putnbr(va_arg(*args, int));
    } else if (spec == 'u') {
        count += my_putnbr_base((unsigned long)va_arg(*args, unsigned int), "0123456789");
    } else if (spec == 'o') {
        count += my_putnbr_base((unsigned long)va_arg(*args, unsigned int), "01234567");
    } else if (spec == 'x') {
        count += my_putnbr_base((unsigned long)va_arg(*args, unsigned int), "0123456789ABCDEF");
    } else if (spec == 'c') {
        count += my_putchar((char)va_arg(*args, int));
    } else if (spec == 's') {
        count += my_putstr(va_arg(*args, char *));
    } else if (spec == 'p') {
        ssize_t w = write(1, "0x", 2);
        if (w > 0) count += (int)w;
        count += my_putnbr_base((unsigned long)va_arg(*args, void *), "0123456789abcdef");
    } else {
        count += my_putchar(spec);
    }

    return count;
}


int my_printf(const char *format, ...)
{
    va_list args;
    int total = 0;

    if (!format)
        return -1; 

    va_start(args, format);

    for (int i = 0; format[i]; i++) {
        if (format[i] == '%' && format[i + 1]) {
            
            i++;
            total += handle_format(format[i], &args);
        } else {
            write(1, &format[i], 1);
            total++;
        }
    }

    va_end(args);
    return total;
}


