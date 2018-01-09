%global __provides_exclude_from ^%{_libdir}/io.elementary.code/.*\\.so$

%global srcname scratch
%global appname io.elementary.code

Name:           elementary-code
Summary:        The text editor that works
Version:        2.4.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)


%if %{?fedora} == 24
BuildRequires:  pkgconfig(libvala-0.32)
%endif

%if %{?fedora} == 25
BuildRequires:  pkgconfig(libvala-0.34)
%endif

%if %{?fedora} == 26
BuildRequires:  pkgconfig(libvala-0.36)
%endif

%if %{?fedora} == 27
BuildRequires:  pkgconfig(libvala-0.38)
%endif

%if %{?fedora} > 27
BuildRequires:  pkgconfig(libvala-0.40)
%endif

Requires:       hicolor-icon-theme

Obsoletes:      scratch-text-editor
Provides:       scratch-text-editor


%description
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible.
Keep things super lightweight and simple, or install extensions to turn
Scratch into a full-blown IDE; it's your choice. And with a handful of
useful preferences, you can tweak the behavior and interface to your
liking.

It's elementary. Scratch is made to be the perfect text editor for
elementary, meaning it closely follows the high standards of design,
speed, and consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala,
scripting with PHP, or marking things up in HTML, Scratch has you
covered. Experience full syntax highlighting with nearly all
programming, scripting, and markup languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS,
.Desktop, Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua,
Makefile, Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

Scratch needs to be translated. Go to Translations to help us providing
this software in your language!


%package        devel
Summary:        The text editor that works
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

This package contains the development headers.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/
%{_libdir}/libcodecore.so.0
%{_libdir}/libcodecore.so.0.0

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%files devel
%{_includedir}/io.elementary.code/

%{_libdir}/libcodecore.so
%{_libdir}/pkgconfig/codecore.pc

%{_datadir}/vala/vapi/codecore.deps
%{_datadir}/vala/vapi/codecore.vapi


%changelog
* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.170232.0d7cbb8a-1
- Update to latest snapshot.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-2
- Adapt to upstream file changes.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-2
- Remove icon cache scriptlets.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180105.001608.fc57a13d-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git171219.151614.17101d60-1
- Initial package.


