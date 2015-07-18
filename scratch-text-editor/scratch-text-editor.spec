%define rev 1523

Summary: Scratch - the text editor that works.
Name: vocal
Version: 2.2.0~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/vocal

Source0: %{name}-%{version}.tar.gz
Source1: make-srpm.sh

BuildRequires: cmake pkgconfig
# BuildRequires: vala gettext
# BuildRequires: desktop-file-utils
# BuildRequires: libappstream-glib


%description
Scratch is the text editor that works for you. It auto-saves your files, meaning they're always up-to-date. Plus it remembers your tabs so you never lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible. Keep things super lightweight and simple, or install extensions to turn Scratch into a full-blown IDE; it's your choice. And with a handful of useful preferences, you can tweak the behavior and interface to your liking.

It's elementary. Scratch is made to be the perfect text editor for elementary, meaning it closely follows the high standards of design, speed, and consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala, scripting with PHP, or marking things up in HTML, Scratch has you covered. Experience full syntax highlighting with nearly all programming, scripting, and markup languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS, .Desktop, Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua, Makefile, Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

Scratch needs to be translated. Go to Translations to help us providing this software in your language!

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/vocal.desktop
# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/vocal.desktop.appdata.xml

# %%find_lang scratch-text-editor


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
# /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
# /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files


%changelog

