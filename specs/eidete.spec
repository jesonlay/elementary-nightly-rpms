Summary:        A simple screencasting app for the elementary project
Name:           eidete
Version:        0.1~rev%{rev}
Release:        3%{?dist}
License:        GPLv2
URL:            http://launchpad.net/eidete

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

Requires:       contractor


%description
Current features
 - encoding to webm
 - selection of the area to be recorded
 - display of the pressed keys
 - audio recording

Todo:
 - create new contracts for facebook, youtube and others (waiting for gnome-online-accounts to be ready)
 - improve and internationalize the key view


%prep
%autosetup


%build
export CFLAGS="-fPIC $RPM_OPT_FLAGS"
export LDFLAGS="-fPIC $RPM_OPT_FLAGS"

%cmake
%make_build


%install
%make_install
%find_lang eidete

%clean
rm -rf %{buildroot}


%post
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%files -f eidete.lang
%doc README

%{_bindir}/eidete
%{_bindir}/videobin-uploader

%{_datadir}/applications/eidete.desktop
%{_datadir}/contractor/videobin.contract
%{_datadir}/icons/hicolor/*/apps/eidete.svg
%{_datadir}/icons/hicolor/48x48/apps/videobin.svg


%changelog
* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev206-3
- Update for packaging changes.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev206-2
- Update for packaging changes.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com>
- Add new res icons.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev206-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev205-2
- Update for packaging changes.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev205-1
- Update to latest snapshot.

* Thu Jun 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev204-1
- Update to latest snapshot.

* Wed Jun 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev203-1
- Update to latest snapshot.

* Sun Jun 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev202-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev201-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev201-2
- Update for packaging changes.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev201-1
- Update to latest snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev201-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev200-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev199-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev198-1
- Update to new upstream snapshot.

* Sat Oct 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev197-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev196-1
- Try to fix f23-x64 build.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev196-2
- rebuild trigger for granite soname bump

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev196-1
- Initial package.

