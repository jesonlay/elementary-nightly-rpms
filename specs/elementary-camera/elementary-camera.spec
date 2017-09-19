Name:           elementary-camera
Summary:        Fast and beautiful camera app
Version:        0.3.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3
URL:            https://github.com/elementary/camera

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)

Provides:       snap-photobooth
Obsoletes:      snap-photobooth


%description
A fast and beautiful camera app.


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

%find_lang pantheon-camera


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/*.appdata.xml


%files -f pantheon-camera.lang
%{_bindir}/pantheon-camera

%{_datadir}/applications/org.pantheon.camera.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.camera.gschema.xml
%{_datadir}/metainfo/org.pantheon.camera.appdata.xml


%changelog
* Tue Sep 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170704.192116.7bb3dae9-1
- Update to version 0.3.0.1.


