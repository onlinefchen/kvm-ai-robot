# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 11:22:59

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 226
- **总 Thread 数**: 30
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 21 threads (201 邮件)
- **RFC**: 1 threads (1 邮件)
- **Bug Report**: 1 threads (1 邮件)
- **GIT PULL**: 3 threads (7 邮件)
- **Other**: 4 threads (16 邮件)

---

## 📌 PATCH

共 21 个 thread

---

### Thread 1: [PATCH v13 00/20] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs

**📧 邮件数**: 37 | **👥 参与者**: 6 | **📅 开始时间**: Wed,  9 Jul 2025 11:59:26 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）的补丁系列，主要内容是为非 CoCo 虚拟机启用主机用户空间对基于 guest_memfd 的内存的映射。以下是讨论的主要内容：

1. **补丁内容**：补丁系列的核心是启用主机用户空间对 guest_memfd 支持的内存进行 mmap() 操作。这一功能将简化虚拟机监控器（VMM）的设计，并增强安全性，防止类似 Spectre 的攻击。

2. **历史讨论要点**：之前的讨论集中在如何将 guest_memfd 的支持扩展到非私有内存，并对现有的 KVM 结构进行重构，以便更好地支持这一新特性。补丁还包括对相关配置选项的重命名，以更准确地反映其功能。

3. **本周新讨论和进展**：本周的讨论主要集中在补丁的具体实现和测试上，包括：
   - 引入新的 KVM 能力 KVM_CAP_GMEM_MMAP，以指示用户空间支持 guest_memfd 的映射。
   - 对 x86 和 arm64 架构的支持进行了详细讨论，确保这些架构能够正确处理基于 guest_memfd 的页面故障。
   - 讨论了如何处理可能的竞争条件和错误情况，确保在内存映射过程中不会出现数据不一致的情况。
   - 提出了对自测功能的扩展，以验证 mmap 操作的正确性和稳定性。

总的来说，本周的讨论推动了 KVM 对 guest_memfd 支持的进一步发展，确保其在不同架构上的一致性和可靠性。

#### 📝 邮件列表

1. **[07-09 11:59]** [PATCH v13 00/20] KVM: Enable host userspace mapping for
 guest_memfd-backed memory for non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-09 11:59]** [PATCH v13 01/20] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[07-09 11:59]** [PATCH v13 02/20] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[07-09 11:59]** [PATCH v13 03/20] KVM: Introduce kvm_arch_supports_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[07-09 11:59]** [PATCH v13 04/20] KVM: x86: Introduce kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-09 11:59]** [PATCH v13 05/20] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[07-09 11:59]** [PATCH v13 06/20] KVM: Fix comments that refer to slots_lock
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[07-09 11:59]** [PATCH v13 07/20] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[07-09 11:59]** [PATCH v13 08/20] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[07-09 11:59]** [PATCH v13 09/20] KVM: guest_memfd: Track guest_memfd mmap support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[07-09 11:59]** [PATCH v13 10/20] KVM: x86/mmu: Generalize private_max_mapping_level
 x86 op to max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[07-09 11:59]** [PATCH v13 11/20] KVM: x86/mmu: Allow NULL-able fault in kvm_max_private_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[07-09 11:59]** [PATCH v13 12/20] KVM: x86/mmu: Consult guest_memfd when computing max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[07-09 11:59]** [PATCH v13 13/20] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[07-09 11:59]** [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default VM type
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[07-09 11:59]** [PATCH v13 15/20] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[07-09 11:59]** [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[07-09 11:59]** [PATCH v13 17/20] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[07-09 11:59]** [PATCH v13 18/20] KVM: Introduce the KVM capability KVM_CAP_GMEM_MMAP
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[07-09 11:59]** [PATCH v13 19/20] KVM: selftests: Do not use hardcoded page sizes in
 guest_memfd test
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[07-09 11:59]** [PATCH v13 20/20] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[07-11 09:14]** Re: [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: kernel test robot <lkp@intel.com>
23. **[07-11 14:04]** Re: [PATCH v13 09/20] KVM: guest_memfd: Track guest_memfd mmap
 support in memslot
   - 发件人: Shivank Garg <shivankg@amd.com>
24. **[07-11 14:18]** Re: [PATCH v13 18/20] KVM: Introduce the KVM capability
 KVM_CAP_GMEM_MMAP
   - 发件人: Shivank Garg <shivankg@amd.com>
25. **[07-11 11:36]** Re: [PATCH v13 10/20] KVM: x86/mmu: Generalize
 private_max_mapping_level x86 op to max_mapping_level
   - 发件人: David Hildenbrand <david@redhat.com>
26. **[07-11 11:38]** Re: [PATCH v13 11/20] KVM: x86/mmu: Allow NULL-able fault in
 kvm_max_private_mapping_level
   - 发件人: David Hildenbrand <david@redhat.com>
27. **[07-11 11:45]** Re: [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: David Hildenbrand <david@redhat.com>
28. **[07-11 09:59]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
29. **[07-11 12:08]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
30. **[07-11 12:09]** Re: [PATCH v13 14/20] KVM: x86: Enable guest_memfd mmap for default
 VM type
   - 发件人: Fuad Tabba <tabba@google.com>
31. **[07-11 14:25]** Re: [PATCH v13 15/20] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[07-11 14:49]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[07-11 15:17]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
34. **[07-11 15:25]** Re: [PATCH v13 17/20] KVM: arm64: Enable host mapping of shared guest_memfd memory
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[07-11 15:34]** Re: [PATCH v13 17/20] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
36. **[07-11 16:48]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[07-11 17:37]** Re: [PATCH v13 16/20] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes

**📧 邮件数**: 30 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  8 Jul 2025 10:25:05 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的多个补丁（PATCH v3 00/27），主要集中在 SCTLR2、DoubleFault2 和 NV（Nested Virtualization）外部中止的修复上。

1. **原始补丁内容**：补丁系列包括对 SCTLR2 和 DoubleFault2 特性的支持，以及对外部中止处理的改进，确保在虚拟化环境中正确处理异常和中止。

2. **历史讨论要点**：之前的讨论中，开发者们关注了如何在 KVM 中实现对新特性的支持，特别是如何处理 SError 异常的路由和掩码。补丁中提出了多项改进，包括在不同上下文中正确设置异常处理的上下文，以及如何在虚拟机中处理未掩码的 SError。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的具体实现上，包括：
   - 增加了对 SCTLR2 和 DoubleFault2 特性的检测。
   - 引入了新的帮助函数以简化嵌套上下文的识别。
   - 讨论了如何在 KVM 中处理带有待处理 SError 的 vCPU，使其在适当情况下被视为可运行。
   - 进行了针对 SError 和 SEA（Synchronous External Abort）处理的增强，确保在特定条件下将异常正确路由到 SError 向量。
   - 添加了自测试以验证 SError 注入和 SEA 路由的正确性。

最终，所有补丁已被应用，标志着对 ARM64 KVM 的重要功能增强。

#### 📝 邮件列表

1. **[07-08 10:25]** [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-08 10:25]** [PATCH v3 01/27] arm64: Detect FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-08 10:25]** [PATCH v3 02/27] arm64: Detect FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-08 10:25]** [PATCH v3 03/27] KVM: arm64: Add helper to identify a nested context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-08 10:25]** [PATCH v3 04/27] KVM: arm64: Treat vCPU with pending SError as runnable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-08 10:25]** [PATCH v3 05/27] KVM: arm64: nv: Respect exception routing rules for SEAs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-08 10:25]** [PATCH v3 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-08 10:25]** [PATCH v3 07/27] KVM: arm64: nv: Add FEAT_RAS vSError sys regs to table
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-08 10:25]** [PATCH v3 08/27] KVM: arm64: nv: Use guest hypervisor's vSError state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[07-08 10:25]** [PATCH v3 09/27] KVM: arm64: nv: Advertise support for FEAT_RAS
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[07-08 10:25]** [PATCH v3 10/27] KVM: arm64: nv: Describe trap behavior of SCTLR2_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[07-08 10:25]** [PATCH v3 11/27] KVM: arm64: Wire up SCTLR2_ELx sysreg descriptors
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[07-08 10:25]** [PATCH v3 12/27] KVM: arm64: Context switch SCTLR2_ELx when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[07-08 10:25]** [PATCH v3 13/27] KVM: arm64: Enable SCTLR2 when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[07-08 10:25]** [PATCH v3 14/27] KVM: arm64: Describe SCTLR2_ELx RESx masks
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[07-08 10:25]** [PATCH v3 15/27] KVM: arm64: Factor out helper for selecting exception target EL
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
17. **[07-08 10:25]** [PATCH v3 16/27] KVM: arm64: nv: Ensure Address size faults affect correct ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[07-08 10:25]** [PATCH v3 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[07-08 10:25]** [PATCH v3 18/27] KVM: arm64: nv: Take "masked" aborts to EL2 when HCRX_EL2.TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[07-08 10:25]** [PATCH v3 19/27] KVM: arm64: nv: Honor SError routing effects of SCTLR2_ELx.NMEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
21. **[07-08 10:25]** [PATCH v3 20/27] KVM: arm64: nv: Enable vSErrors when HCRX_EL2.TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
22. **[07-08 10:25]** [PATCH v3 21/27] KVM: arm64: Advertise support for FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
23. **[07-08 10:25]** [PATCH v3 22/27] KVM: arm64: Advertise support for FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
24. **[07-08 10:25]** [PATCH v3 23/27] KVM: arm64: Don't retire MMIO instruction w/ pending (emulated) SError
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
25. **[07-08 10:25]** [PATCH v3 24/27] KVM: arm64: selftests: Add basic SError injection test
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
26. **[07-08 10:25]** [PATCH v3 25/27] KVM: arm64: selftests: Test SEAs are taken to SError vector when EASE=1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
27. **[07-08 10:25]** [PATCH v3 26/27] KVM: arm64: selftests: Add SCTLR2_EL1 to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[07-08 10:25]** [PATCH v3 27/27] KVM: arm64: selftests: Catch up set_id_regs with the kernel
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
29. **[07-08 10:39]** Re: [PATCH v3 08/27] KVM: arm64: nv: Use guest hypervisor's vSError
 state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
30. **[07-08 12:00]** Re: [PATCH v3 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 3: [PATCH v3 00/22] ARM64 PMU Partitioning

**📧 邮件数**: 17 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 26 Jun 2025 20:04:36 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 PMU（性能监控单元）分区的新补丁系列，旨在为虚拟机提供更直接的计数器访问，从而显著降低开销。补丁的主要内容包括创建一个新的 PMU 方案，允许为客户机保留一部分计数器。

在历史讨论中，Colton Lewis 提出了多个补丁，涵盖了对 ARM64 CPU 特性、PMU 计数器的分区方法以及 KVM 与 PMU 之间的接口清理等方面的修改。讨论中提到的关键点包括如何处理 PMU 计数器的访问权限，以及在不同环境下（如 nVHE 和 VHE）对 HPMN（计数器保留数量）的配置。

在本周的新讨论中，参与者 Mark Rutland 对补丁中的一些细节表示认可，并提出了小的修改建议，如去掉某些前缀以保持一致性。此外，Oliver Upton 提出了对命名的看法，认为当前的“分区”命名可能不够准确，建议使用“pmu-direct”来更好地描述功能。整体来看，补丁系列正在逐步完善，参与者们关注细节并进行积极讨论，以确保最终实现的清晰性和有效性。

#### 📝 邮件列表

1. **[06-26 20:04]** [PATCH v3 00/22] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[06-26 20:04]** [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[06-26 20:04]** [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-26 20:04]** [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-26 20:04]** [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-26 20:04]** [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[07-07 17:05]** Re: [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Mark Rutland <mark.rutland@arm.com>
8. **[07-07 17:07]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[07-07 17:13]** Re: [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Mark Rutland <mark.rutland@arm.com>
10. **[07-07 17:57]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Mark Rutland <mark.rutland@arm.com>
11. **[07-07 17:58]** Re: [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Mark Rutland <mark.rutland@arm.com>
12. **[07-07 12:07]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[07-08 22:34]** Re: [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[07-08 22:37]** Re: [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[07-08 22:38]** Re: [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[07-08 22:38]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[07-08 15:41]** Re: [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 4: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 16 | **👥 参与者**: 6 | **📅 开始时间**: Sat, 5 Jul 2025 07:17:11 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于将 GPU 设备内存映射为可缓存的 KVM（内核虚拟机）改进，主要涉及一系列补丁（PATCH v10 0/6）。这些补丁的核心目的是支持在 arm64 架构上更有效地管理 GPU 设备内存，以提高性能和安全性。

在历史讨论中，Ankit Agrawal 提出了多个补丁，主要包括：
1. 将设备变量重命名为 `s2_force_noncacheable`，以更准确地反映其功能。
2. 更新检测设备内存的检查方法，以更好地支持缓存维护操作。
3. 阻止可缓存的 PFNMAP 映射，解决 S1 和 S2 映射属性不匹配的安全问题。
4. 允许通过 VMA 标志进行可缓存的二级映射。
5. 引入新的 KVM 能力，以支持可缓存的 PFNMAP。

本周的新讨论中，多个参与者（如 Catalin Marinas、David Hildenbrand 和 Jason Gunthorpe）对补丁系列进行了审查并表示认可。Ankit 感谢他们的反馈，并询问 Oliver Upton 是否可以将这些补丁应用到下一个版本中。Oliver 确认已对补丁进行了最终的修改和应用，表示感谢参与者的努力。

综上所述，该讨论的进展表明补丁已获得广泛认可，并成功应用于下一版本，标志着对 KVM 在 arm64 上的 GPU 内存管理的改进。

#### 📝 邮件列表

1. **[07-05 07:17]** [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[07-05 07:17]** [PATCH v10 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[07-05 07:17]** [PATCH v10 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[07-05 07:17]** [PATCH v10 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[07-05 07:17]** [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
6. **[07-05 07:17]** [PATCH v10 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>
7. **[07-06 19:51]** Re: [PATCH v10 1/6] KVM: arm64: Rename the device variable to
 s2_force_noncacheable
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
8. **[07-06 19:52]** Re: [PATCH v10 2/6] KVM: arm64: Update the check to detect device
 memory
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[07-06 19:54]** Re: [PATCH v10 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[07-06 20:00]** Re: [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping
 using VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[07-06 20:02]** Re: [PATCH v10 6/6] KVM: arm64: Expose new KVM cap for cacheable
 PFNMAP
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[07-07 09:32]** Re: [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: David Hildenbrand <david@redhat.com>
13. **[07-07 09:27]** Re: [PATCH v10 5/6] KVM: arm64: Allow cacheable stage 2 mapping
 using VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
14. **[07-07 16:39]** Re: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
15. **[07-07 16:57]** Re: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[07-09 14:34]** Re: [PATCH v10 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 5: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory

**📧 邮件数**: 11 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 24 Jun 2025 16:40:18 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 的补丁（PATCH v12 10/18），旨在处理使用共享内存的 guest_memfd 的页面错误。补丁的核心是增强 KVM 对于共享内存的支持，以便在处理页面错误时能够更好地管理内存。

在历史讨论中，参与者们探讨了补丁的具体实现细节和潜在用例。例如，Ackerley Tng 提出了在同一虚拟机中同时支持不支持 mmap 的 memslot 的需求，Shivank Garg 则强调了在实现 mmap 功能后再处理复杂用例的策略。多位参与者一致认为，首先应将 mmap 功能合并到主干中，然后再逐步完善。

在本周的新讨论中，Sean Christopherson 和 Ackerley Tng 继续围绕补丁的实现进行深入探讨。Sean 提出了对 KVM 内部架构钩子的修改建议，并讨论了如何在不增加复杂性的前提下，处理共享和私有内存的跟踪问题。Ackerley Tng 则表示将很快重新提交补丁，并感谢大家的澄清和建议。

总体来看，讨论围绕补丁的实现细节、用例和未来的迭代展开，参与者们对补丁的方向表示支持，并期待后续的进展。

#### 📝 邮件列表

1. **[06-24 16:40]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
2. **[06-27 08:01]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
3. **[06-30 09:07]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-30 07:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
5. **[06-30 16:08]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[07-01 00:56]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Shivank Garg <shivankg@amd.com>
7. **[06-30 22:03]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: David Hildenbrand <david@redhat.com>
8. **[07-01 07:15]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
9. **[07-01 16:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: David Hildenbrand <david@redhat.com>
10. **[07-07 17:05]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[07-08 06:44]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 6: [PATCH v2 02/15] KVM: selftests: Enable selftests runner to find
 executables in different path

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 9 Jul 2025 14:39:05 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 自测试运行器的补丁（PATCH v2 02/15），旨在使其能够在不同路径中查找可执行文件。该补丁的核心是增强自测试运行器的灵活性，使其能够处理不同的可执行文件路径。

在之前的讨论中，参与者主要关注补丁的命名和功能设计。例如，Sean Christopherson 提到“executable”这个术语可能会引起误解，建议使用更符合 Linux 习惯的“--path”参数。此外，关于如何处理命令行选项的设计也引发了讨论，特别是如何简化输出选项以提高用户体验。

本周的新讨论中，Sean Christopherson 对补丁的具体实现提出了一些建议，包括如何处理超时的输出、改进日志记录的方式，以及对命令行参数的进一步简化。他建议将输出选项合并为更少的布尔值，以便用户能够更灵活地控制输出内容。同时，Oliver Upton 提出了对默认测试用例的生成和管理的看法，认为应该优先考虑减少噪音，避免在树中提交过多的默认测试配置。

总体来看，本周的讨论集中在如何优化补丁的实现细节和用户体验上，参与者们积极提出改进建议，以确保 KVM 自测试运行器的功能更加完善。

#### 📝 邮件列表

1. **[07-09 14:39]** Re: [PATCH v2 02/15] KVM: selftests: Enable selftests runner to find
 executables in different path
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-09 14:46]** Re: [PATCH v2 03/15] KVM: selftests: Add timeout option in selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[07-09 14:52]** Re: [PATCH v2 04/15] KVM: selftests: Add option to save selftest
 runner output to a directory
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[07-09 14:55]** Re: [PATCH v2 06/15] KVM: selftests: Add a flag to print only test
 status in KVM Selftests run
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[07-09 15:01]** Re: [PATCH v2 07/15] KVM: selftests: Add various print flags to KVM
 Selftest Runner
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[07-09 15:25]** Re: [PATCH v2 00/15] Add KVM Selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[07-09 15:25]** Re: [PATCH v2 03/15] KVM: selftests: Add timeout option in selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[07-09 16:06]** Re: [PATCH v2 11/15] KVM: selftests: Auto generate default tests for
 KVM Selftests Runner
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-09 17:18]** Re: [PATCH v2 11/15] KVM: selftests: Auto generate default tests for
 KVM Selftests Runner
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[07-09 17:20]** Re: [PATCH v2 01/15] KVM: selftest: Create KVM selftest runner
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 7: [PATCH 0/2] Fix and add warning of misuse of type##_replace_bits()

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Thu,  3 Jul 2025 14:57:27 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 `type##_replace_bits()` 函数的修复和使用警告的补丁。历史讨论中，Ben Horgan 提出了两个补丁：第一个补丁修复了 `u64_replace_bits()` 的使用错误，并在 `bitfield.h` 中添加了 `__must_check` 注解，以确保返回值被检查。第二个补丁进一步强调了 `type##_replace_bits()` 的返回值检查的重要性。

在本周的新讨论中，Yury Norov 提出了是否也应将 `_encode_bits()` 和 `_get_bits()` 函数标记为 `__must_check` 的建议，认为从统一性角度来看这样做是有意义的。Ben Horgan 对此表示可以考虑，但认为这些函数的风险较小，可能不需要强制检查。Marc Zyngier 确认第一个补丁将通过 KVM/arm64 树合并，并预计作为 6.16 版本的修复。Yury Norov 表示将自行处理第二个补丁的 v2 版本。

此外，Oliver Upton 提出了两个新的补丁，旨在修复和测试 SError 的 ESR 传播问题，并已被应用到下一版本中。整体来看，本周的讨论主要集中在补丁的细节和后续版本的处理上。

#### 📝 邮件列表

1. **[07-03 14:57]** [PATCH 0/2] Fix and add warning of misuse of type##_replace_bits()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[07-03 14:57]** [PATCH 2/2] bitfield: Ensure the return value of type##_replace_bits() is checked
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[07-07 12:31]** Re: [PATCH 2/2] bitfield: Ensure the return value of
 type##_replace_bits() is checked
   - 发件人: Yury Norov <yury.norov@gmail.com>
4. **[07-08 10:42]** Re: [PATCH 2/2] bitfield: Ensure the return value of
 type##_replace_bits() is checked
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[07-08 10:45]** Re: [PATCH 2/2] bitfield: Ensure the return value of type##_replace_bits() is checked
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-08 10:46]** Re: [PATCH 2/2] bitfield: Ensure the return value of
 type##_replace_bits() is checked
   - 发件人: Yury Norov <yury.norov@gmail.com>
7. **[07-08 16:06]** [PATCH 0/2] KVM: arm64: Fix + test for SError ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-08 16:06]** [PATCH 1/2] KVM: arm64: Populate ESR_ELx.EC for emulated SError injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-08 16:06]** [PATCH 2/2] KVM: arm64: selftests: Test ESR propagation for vSError injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[07-09 09:59]** Re: [PATCH 0/2] KVM: arm64: Fix + test for SError ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 8: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 11 Jul 2025 12:39:50 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理同步外部中止（SEA）的补丁。补丁的核心内容是当 APEI（ACPI Platform Error Interface）无法处理 SEA 时，KVM 可以选择将控制权转交给用户空间，以便更优雅地处理内存错误，避免虚拟机崩溃。

在历史讨论中，补丁的背景被阐述，指出当前处理 SEA 的方式会导致虚拟机内核崩溃，且在某些情况下（如可恢复的未更正内存错误），存在更好的处理方式。补丁引入了一个新的用户空间可见特性 `KVM_CAP_ARM_SEA_TO_USER`，允许 VMM（虚拟机监控器）在发生 SEA 时退出到用户空间，从而提供更多的控制和观察能力。

在本周的新讨论中，参与者对补丁进行了深入的审查和修改建议。Oliver Upton 提出了避免在头文件中添加单一调用点的辅助函数，并建议在补丁中增加对 FEAT_RAS（Reliability, Availability, and Serviceability）特性的详细说明。此外，讨论还涉及如何处理由于 VNCR（Virtual Network Control Register）引起的 SEA，以及如何在用户空间中注入外部中止的相关问题。

总体来看，本周的讨论集中在补丁的细节修改和潜在的扩展上，参与者们积极交流，推动补丁的完善。

#### 📝 邮件列表

1. **[07-11 12:39]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-11 12:42]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-11 12:44]** Re: [PATCH v2 5/6] KVM: selftests: Test for KVM_CAP_INJECT_EXT_IABT
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-11 16:58]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[07-11 16:59]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
6. **[07-11 16:59]** Re: [PATCH v2 5/6] KVM: selftests: Test for KVM_CAP_INJECT_EXT_IABT
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
7. **[07-12 12:47]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-12 12:57]** Re: [PATCH v2 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[07-12 19:42]** Re: [PATCH v2 3/6] KVM: arm64: Allow userspace to inject external
 instruction aborts
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 9: [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  9 Jul 2025 14:14:11 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目的是允许用户空间写入 GICD_TYPER2.nASSGIcap 寄存器。

**原始补丁内容**：
补丁系列的核心是允许用户空间在初始化 VGIC（虚拟通用中断控制器）之前修改 GICD_TYPER2.nASSGIcap 寄存器的值，以便控制虚拟处理单元（vPE）的分配。这对于在资源受限的环境中管理虚拟机的功能非常重要。

**之前讨论要点**：
在历史讨论中，参与者们探讨了如何在不影响运行中的虚拟机的情况下，允许用户空间访问某些 ID 类寄存器。讨论还涉及到 GICD_IIDR 寄存器的访问权限问题，确保在初始化前可以安全地进行修改。

**本周新讨论与进展**：
本周的讨论集中在补丁的最终版本上，Oliver Upton 提到希望尽快将此功能合并到 6.17 版本中。补丁中新增了多个功能，包括对 vSGIs 和 vLPIs 的支持，以及对 GICD_IIDR 寄存器的访问权限调整。此外，Raghavendra Rao Ananta 提交了针对 nASSGIcap 属性的自测代码，确保在 VGIC 初始化前可以合理地配置该属性，并且在初始化后无法修改。最后，文档也更新了对这些寄存器访问的用户空间预期的描述。

整体来看，本周的讨论推动了补丁的完善，并为未来的版本整合奠定了基础。

#### 📝 邮件列表

1. **[07-09 14:14]** [PATCH v4 0/6] KVM: arm64: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[07-09 14:14]** [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v. vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[07-09 14:14]** [PATCH v4 2/6] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ handling
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[07-09 14:14]** [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR prior to initialization
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[07-09 14:14]** [PATCH v4 4/6] KVM: arm64: vgic-v3: Allow userspace to write GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[07-09 14:14]** [PATCH v4 5/6] KVM: arm64: selftests: Add test for nASSGIcap attribute
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[07-09 14:14]** [PATCH v4 6/6] Documentation: KVM: arm64: Describe VGICv3 registers writable pre-init
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[07-10 09:59]** Re: [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v.
 vLPIs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[07-10 09:22]** Re: [PATCH v4 1/6] KVM: arm64: Disambiguate support for vSGIs v.
 vLPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 10: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 20:41:42 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构的 HIP10/HIP10C erratum 162200803 的补丁。该补丁旨在解决 GICv4.0 中的一个 SoC 错误，具体表现为在多个虚拟处理单元（vPE）同时发送调度命令时，可能会导致某些命令未被调度，从而引发超时问题。

在历史讨论中，Zhou Wang 提出了补丁的初步方案，Marc Zyngier 则指出该方案未能完全解决问题，特别是在 KVM 中未对虚拟 LPI 的数量进行限制。双方讨论了在 MAPTI/MAPI 命令中增加对 LPI 数量的检查，以及在虚拟机迁移时如何处理 GICD_TYPER 的配置。

本周的新讨论中，Zhou Wang 提出了将 GICD_TYPER.num_LPIs 设置为可写字段的想法，并表示如果在虚拟机之间的 num_LPI 配置不同，则迁移将失败。Marc Zyngier 认可了这一思路，并指出在非故障系统中，num_LPIs 应始终可写。最终，Zhou Wang 表示将准备新的补丁以实现这一方案。

总结而言，讨论围绕如何在内核中实现对该 erratum 的支持展开，双方达成了一致，Zhou Wang 将继续推进补丁的开发。

#### 📝 邮件列表

1. **[06-26 20:41]** [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[06-26 14:27]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-27 14:36]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[07-01 09:14]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-02 17:57]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
6. **[07-03 11:44]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[07-08 20:05]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
8. **[07-08 13:47]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[07-09 10:08]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 11: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 2 Jul 2025 10:37:50 +1000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM64 架构下的 RME（Realm Management Extensions）功能，特别是允许虚拟机监控器（VMM）设置 RIPAS（Realm Initialization Permission Access Settings）。该讨论的原始补丁是针对这一功能的实现，旨在增强虚拟化支持。

在历史讨论中，参与者对补丁进行了细致的审查，提出了多个小的修改建议，主要集中在代码的清晰性和可维护性上。Gavin Shan 和 Suzuki K Poulose 等人对补丁的整体方向表示认可，并提出了一些具体的代码改进建议。

在本周的新讨论中，Steven Price 对之前的反馈做出了回应，表示同意大部分修改意见，并讨论了 RMMv1.1 规范中新增的 RMI_RTT_SET_S2AP 选项，认为这为枚举类型的扩展提供了可能性。此外，Gavin Shan 也表示对 RMMv1.1 的实现还在学习中，显示出对该补丁的持续关注和对未来扩展的期待。

总体来看，本周的讨论进一步推动了补丁的完善，参与者们在代码细节和规范理解上达成了一定的共识，为补丁的最终提交奠定了基础。

#### 📝 邮件列表

1. **[07-02 10:37]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[07-03 14:22]** Re: [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[07-09 15:42]** Re: [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
4. **[07-09 15:42]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
5. **[07-09 15:49]** Re: [PATCH v9 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[07-09 16:29]** Re: [PATCH v9 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
7. **[07-10 15:24]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>

---

### Thread 12: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 27 Jun 2025 14:49:30 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下阻止可缓存 PFNMAP 映射的补丁（PATCH v9 3/6）。该补丁旨在解决 arm64 的 get_vma_page_shift() 函数错误地假设 VM_PFNMAP VMA 是物理连续的问题，这可能导致映射不一致。

在历史讨论中，参与者们探讨了 KVM 是否应该依赖主机来发现映射的连续性，并提出不应增加新的标志。Jason Gunthorpe 强调了继续推进 Peter Xu 的工作，以便 PFNMAP 使用大 PTEs 的重要性。Will Deacon 则提出了对 MMU 通知的疑问，关注如何确保在使用 remap_pfn_range() 时不会出现过时的映射问题。

在本周的新讨论中，Will Deacon 发现自己之前误解了 remap_pfn_range() 的行为，认为它会自动取消现有映射，但实际上并非如此。这一发现有助于澄清之前的讨论，并推动对补丁的理解。

总体来看，讨论围绕如何优化 KVM 的映射机制展开，参与者们对补丁的方向和实现细节进行了深入的交流。

#### 📝 邮件列表

1. **[06-27 14:49]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>
2. **[06-30 01:56]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
3. **[06-30 09:25]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
4. **[07-04 14:21]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: David Hildenbrand <david@redhat.com>
5. **[07-04 17:04]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>
6. **[07-04 13:47]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
7. **[07-08 13:47]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 13: [PATCH] KVM: arm64: fix u64_replace_bits() usage

**📧 邮件数**: 6 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 11 Jul 2025 09:27:47 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 中 arm64 架构下 `u64_replace_bits()` 函数的使用问题。

1. **原始 patch/问题的内容**：
   Arnd Bergmann 提出的补丁旨在修复 `u64_replace_bits()` 函数的使用，该函数返回一个修改后的值，但并不修改其参数。邮件中指出在 `access_mdcr` 函数中，忽略了该函数的返回值，导致潜在的错误。补丁通过将返回值赋给 `val` 来解决此问题。

2. **之前的讨论要点**：
   此次讨论并没有提供历史讨论的上下文，但提到该问题的修复与 Ben Horgan 的补丁相关，表明在此之前已经有类似的修复尝试。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Zenghui Yu 表示 Ben 的补丁已经解决了这个问题。Marc Zyngier 提到他已经为 6.16 版本排队了一个修复，并讨论了补丁在不同分支中的状态。Arnd 进一步澄清了补丁的顺序问题，指出 Ben 的修复可能未被纳入当前的 -next 分支。最后，Mark Brown 强调需要将该修复添加到 -next，以确保在未来的测试中覆盖此问题，避免类似问题的出现。

总体来看，本周的讨论集中在确认补丁的有效性及其在不同版本中的排队状态，确保修复能够及时纳入主线代码中。

#### 📝 邮件列表

1. **[07-11 09:27]** [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Arnd Bergmann <arnd@kernel.org>
2. **[07-11 16:02]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
3. **[07-11 09:36]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-11 10:44]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Arnd Bergmann <arnd@arndb.de>
5. **[07-11 09:53]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[07-11 10:13]** Re: [PATCH] KVM: arm64: fix u64_replace_bits() usage
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 14: [PATCH v3 05/10] KVM: arm64: Add trap configs for PMSDSFR_EL1

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 9 Jul 2025 10:53:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主题为“添加 PMSDSFR_EL1 的陷阱配置”。该补丁的目的是为了处理与 PMSDSFR_EL1 相关的访问控制，确保虚拟机（guest）在正常情况下不会尝试访问该寄存器。

在历史讨论中，参与者 James Clark 提到，正常行为的 guest 不会访问 PMSDSFR_EL1，因为该寄存器的存在会通过访问 PMSDSFR_EL1.FDS 进行检查，而当前该寄存器被设置为 `undef_access`，因此对 guest 隐藏了 SPE（可扩展性能监控）。Joey Gouly 对该补丁表示认可，并给予了审核通过的反馈。

本周的新讨论主要集中在另一个补丁（PATCH v3 08/10），该补丁处理来自主机的 FFA_MEM_LEND 调用。DaeRo Lee 提出了一些关于内存共享和借用的疑问，询问在借用内存后主机是否仍然可以访问这些内存。Will Deacon 回应称，只有在安全域实现存在问题时，主机才会依赖 NS hypervisor 进行隔离，并进一步澄清 pKVM 并不使用 FF-A 来管理主机与 guest 之间的页面所有权。讨论中强调了在进行内存借用操作时，需要确保安全域防止非安全访问，而不依赖于 pKVM 进行阶段二的解除映射。

#### 📝 邮件列表

1. **[07-09 10:53]** Re: [PATCH v3 05/10] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[07-12 22:36]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: DaeRo Lee <skseofh@gmail.com>
3. **[07-13 12:26]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the
 host
   - 发件人: Will Deacon <will@kernel.org>
4. **[07-13 23:59]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: DaeRo Lee <skseofh@gmail.com>
5. **[07-13 21:01]** Re: [PATCH v3 08/10] KVM: arm64: Handle FFA_MEM_LEND calls from the
 host
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 15: [PATCH v2 0/2] Fix and add warning of misuse of type##_replace_bits()

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  9 Jul 2025 10:38:06 +0100

#### 🤖 AI 总结

本邮件线程讨论了两个补丁（patch），旨在修复和增强对 `type##_replace_bits()` 函数的使用警告。

**原始 patch/问题内容**：
补丁的主要目的是修复 `u64_replace_bits()` 的错误用法，并在相关函数上添加 `__must_check` 注释，以确保返回值被检查，从而避免未来的误用。

**之前讨论要点**：
在之前的讨论中，参与者指出 `u64_replace_bits()` 的返回值被忽略，导致其调用无效。为了解决这个问题，补丁将其替换为 `u64p_replace_bits()`，以确保值在原地更新。

**本周的新讨论、进展或结论**：
本周的讨论中，Ben Horgan 提交了两个补丁：
1. 第一个补丁修复了 `MDCR_EL2.HPMN` 的上限强制执行问题，并得到了 Zenghui Yu 的审核和确认。
2. 第二个补丁确保了辅助函数的返回值被检查，添加了 `__must_check` 注释以强制这一用法。该补丁也得到了 Yury Norov 的确认并已应用。

总结来看，本周的讨论主要集中在补丁的确认和应用上，确保了代码的正确性和安全性。

#### 📝 邮件列表

1. **[07-09 10:38]** [PATCH v2 0/2] Fix and add warning of misuse of type##_replace_bits()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[07-09 10:38]** [PATCH v2 1/2] KVM: arm64: Fix enforcement of upper bound on MDCR_EL2.HPMN
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[07-09 10:38]** [PATCH v2 2/2] bitfield: Ensure the return values of helper functions are checked
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[07-09 13:22]** Re: (subset) [PATCH v2 1/2] KVM: arm64: Fix enforcement of upper bound on MDCR_EL2.HPMN
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[07-09 11:33]** Re: [PATCH v2 2/2] bitfield: Ensure the return values of helper
 functions are checked
   - 发件人: Yury Norov <yury.norov@gmail.com>

---

### Thread 16: [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 01 Jul 2025 22:06:33 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 FF-A 1.2 及 SEND_DIRECT2 ABI 的支持，主要通过一系列补丁进行实现。

**原始 patch/问题的内容**：
Per Larsen 提出的补丁集（PATCH v7 0/5）旨在支持 FF-A 1.2 规范，特别是引入新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。补丁的目的是防止主机使用低于已与虚拟机监控器（hypervisor）协商的 FF-A 版本，因为虚拟机监控器缺乏必要的兼容性路径来进行版本转换。

**之前的讨论要点**：
在历史讨论中，Marc Zyngier 对补丁中的某些寄存器处理提出质疑，认为盲目更改这些寄存器可能会导致问题。他强调了 FF-A 规范中对寄存器使用的要求，并对补丁的实现提出了疑虑。

**本周的新讨论、进展或结论**：
在本周的讨论中，Per Larsen 针对 Marc 的质疑进行了回应，引用了 FF-A 规范的相关部分，指出只要将保留寄存器写入零，便符合规范要求。他进一步分析了 FF-A 1.2 规范中关于状态机的内容，认为在处理 FFA_MSG_WAIT 和直接请求 ABI 时，补丁的实现是合理的。整体来看，本周的讨论推动了对补丁的理解，并为其有效性提供了支持。

#### 📝 邮件列表

1. **[07-01 22:06]** [PATCH v7 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-01 22:06]** [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-03 13:38]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization and in host handler
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-07 17:06]** Re: [PATCH v7 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen <perl@immunant.com>

---

### Thread 17: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 4 Jul 2025 18:18:24 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM 架构的性能监控单元（PMU）支持分支记录缓冲扩展（BRBE）的补丁。补丁的主要内容是为 ARM PMU v3 添加对 BRBE 的支持，以增强性能监控能力。

在历史讨论中，Mark Rutland 对补丁表示认可，并提出了一些需要修正的细节，认为补丁整体上已经具备应用的条件。他提到需要在事件溢出时处理 BRBE 的无效化操作，并询问 Will 是否愿意在应用补丁时进行相应的修改。

在本周的新讨论中，Rob Herring 和 Mark Rutland 讨论了 PMU 中断带来的样本不连续性问题，Rob 表示这种不连续性在实际应用中影响不大，因为需要在短时间内发生两个 PMU 中断才能导致样本丢失。Will Deacon 随后确认已将补丁应用到他的分支中，表示感谢并提供了补丁的链接。

总的来说，本周的讨论主要集中在补丁的细节确认和应用进展上，补丁已被成功应用，标志着对 ARM PMU 的 BRBE 支持的进一步推进。

#### 📝 邮件列表

1. **[07-04 18:18]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[07-07 10:57]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
3. **[07-08 19:02]** Re: [PATCH v23 0/4] arm64/perf: Enable branch stack sampling
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 18: [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 25 Jun 2025 17:12:20 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 x86 架构下提供一个能力，以禁用 APERF/MPERF 读取拦截的补丁（PATCH v5 0/5）。该补丁的目的是允许虚拟机监控程序（VMM）授予来宾读取 IA32_APERF 和 IA32_MPERF 的权限，以便来宾能够确定物理 LPU 的有效频率倍增器。

在历史讨论中，Sean Christopherson 提到该补丁系列的最后一部分是为了处理与 arm64 相关的自测更改，并且可以被忽略而不影响 x86 的内容。Jim 的补丁系列是为了实现这一功能，并且与之前的补丁（如 b51700632e0e）相互关联，后者允许用户空间的 VMM 授予来宾对特定 MSR 的读取访问。

在本周的新讨论中，Sean Christopherson 确认已将该补丁应用到 kvm-x86 的杂项分支，并修复了一个拼写错误。此外，他还列出了补丁系列中的各个补丁和相关的提交链接，显示出补丁的具体实现和测试内容。这标志着该补丁的进一步推进和整合。

#### 📝 邮件列表

1. **[06-25 17:12]** [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-10 16:08]** Re: [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF
 read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 19: [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 27 Jun 2025 10:09:01 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 GICv5 主机上启用 GICv3 客户机的补丁（PATCH v2 0/5），主要通过利用 GICv5 的遗留兼容性特性（FEAT_GCIE_LEGACY）来实现。该补丁的主要目的是使现有的 GICv3 虚拟机能够在 GICv5 系统上运行，而无需对虚拟机或虚拟机监控器进行修改。

在历史讨论中，Sascha Bischoff 提出了这一补丁系列，强调了两个主要的改动方向：一是增强 KVM 对 GIC 的支持，以便检测 GICv5 主机并配置其支持 GICv3 客户机；二是确保转发的 PPI 中断能够正常工作。

在本周的新讨论中，Oliver Upton 表示他已经开始处理这些补丁，并将其应用到 -next 分支中。虽然他对这些补丁能否在 6.17 版本中落地表示不确定，但对 KVM 部分的进展感到满意。此外，他还列出了五个具体的补丁，包括对 GICv5 的支持和相关结构的填充等。

总体来看，该讨论围绕着在新的硬件架构上保持向后兼容性展开，旨在提升虚拟化环境的灵活性与兼容性。

#### 📝 邮件列表

1. **[06-27 10:09]** [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[07-08 15:24]** Re: [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using FEAT_GCIE_LEGACY
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v2 08/14] powerpc: Handle KCOV __init vs inline mismatches

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 9 Jul 2025 18:57:00 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 PowerPC 架构的补丁，标题为“[PATCH v2 08/14] powerpc: Handle KCOV __init vs inline mismatches”。该补丁旨在处理 KCOV 在 __init 和内联函数之间的不匹配问题。

在历史讨论中，并没有提供具体的背景信息或之前的讨论内容，邮件列表中仅有本周的新讨论。

本周的讨论中，参与者 Kees Cook 对补丁表示认可，并表示将采用该补丁，放弃自己之前的补丁。这表明该补丁得到了积极的反馈，并可能会被合并到主线代码中。

总结而言，此次邮件讨论主要集中在一个针对 PowerPC 的补丁上，尽管缺乏历史讨论的背景，但本周的反馈显示出该补丁的有效性和被接受的可能性。

#### 📝 邮件列表

1. **[07-09 18:57]** Re: [PATCH v2 08/14] powerpc: Handle KCOV __init vs inline mismatches
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 21: [PATCH v4 05/20] KVM: arm64: timers: Allow physical offset
 without CNTPOFF_EL2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 9 Jul 2025 16:12:18 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的定时器功能，特别是允许在没有 CNTPOFF_EL2 的情况下使用物理偏移。

**原始 patch/问题内容**：
该 patch 的目的是修改 KVM 的定时器实现，以支持在没有 CNTPOFF_EL2 的情况下使用物理偏移。这一修改旨在提升定时器的灵活性和兼容性。

**之前讨论要点**：
在之前的讨论中，Marc Zyngier 提到他在 Kunpeng920 上测试了 arch_timer_edge_cases，并发现 test_timer_cval() 在测试物理定时器时返回的时间过长。他指出，注释中的描述存在错误，应该明确为“将定时器设置为 CVAL=0”。此外，他提到在单独执行该测试时，没有触发物理定时器中断。

**本周的新讨论、进展或结论**：
本周，Zenghui Yu 对 test_timer_cval() 的行为进行了详细分析，指出在执行过程中没有触发物理定时器中断，并依赖于后续的 kvm_timer_vcpu_load() 来捕获定时器到期并向客户机注入中断。他表示这个测试用例并不具备实际应用价值，并对是否需要（或能否）正确模拟该情况表示疑问。整体来看，本周的讨论进一步深入了对定时器功能的理解，但并未形成明确的解决方案或结论。

#### 📝 邮件列表

1. **[07-09 16:12]** Re: [PATCH v4 05/20] KVM: arm64: timers: Allow physical offset
 without CNTPOFF_EL2
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH] tools: Remove obsolete 32-bit arm kvm.h header file

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 10 Jul 2025 12:25:19 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于移除过时的32位ARM KVM头文件（kvm.h）。在历史讨论中，提到原始的32位ARM kvm.h头文件已在提交541ad0150ca4a中被移除，该提交表示不再支持32位KVM主机，因此工具目录中的相应文件也应被删除。

本周的讨论由Thomas Huth发起，他提交了一个RFC补丁，建议删除工具目录下的32位ARM kvm.h头文件。补丁中指出，由于该文件已经不再使用，故应进行清理。补丁中包含了对文件的删除操作，并且标记为RFC（请求反馈），因为他目前没有32位ARM的构建环境，因此未能进行编译测试。

总结来说，本周的进展主要是提出了删除过时文件的补丁，并强调了该文件的冗余性，期待社区的反馈。

#### 📝 邮件列表

1. **[07-10 12:25]** [RFC PATCH] tools: Remove obsolete 32-bit arm kvm.h header file
   - 发件人: Thomas Huth <thuth@redhat.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] WARNING in pend_serror_exception

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 12 Jul 2025 17:06:30 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM ARM64 虚拟化环境中出现的一个警告信息，具体是 `pend_serror_exception` 函数中的警告。该问题由 syzbot 自动检测到，相关的内核版本为 6.16.0-rc3，提交哈希为 15724a984643。

在历史讨论中，虽然没有具体的前期讨论记录，但该警告提示了在处理某些错误时可能存在的问题，表明在 KVM 的错误注入机制中可能存在缺陷。

本周的新讨论中，syzbot 提供了详细的错误报告，包括相关的控制台输出、内核配置和重现步骤。这些信息将帮助开发者定位和修复问题。报告中还提到，如果修复了该问题，开发者应在提交中添加特定的标签，以便追踪。当前没有其他参与者对该问题进行回复或讨论，表明该问题仍在等待进一步的关注和解决。

#### 📝 邮件列表

1. **[07-12 17:06]** [syzbot] [kvmarm?] WARNING in pend_serror_exception
   - 发件人: syzbot <syzbot+1f6f096afda6f4f8f565@syzkaller.appspotmail.com>

---

## 📌 GIT PULL

共 3 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.16, take #4

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 16:20:23 +0100

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.16 版本中的修复补丁，主题为“[GIT PULL] KVM/arm64 fixes for 6.16, take #4”。历史讨论中，Marc Zyngier 提到此次补丁主要包括三个修复：允许 pKVM 初始化失败而不影响主机运行、确保主机 S2 的映射不超过限制，以及针对嵌套 GICv3 模拟的一个小错误修复。

在本周的新讨论中，Paolo Bonzini 确认了补丁的合并，并提到在此期间 git:// 协议出现了问题，建议使用 https:// 进行访问。Marc Zyngier 对此表示困惑，并询问是否有相关公告，随后他自己测试了 git:// 协议并成功克隆了代码库。最终，Paolo 也确认该协议现在可以正常使用，认为之前的问题可能是偶发的。

总结而言，此次讨论主要围绕 KVM/arm64 的修复补丁及其合并进展，期间还涉及到版本控制系统的访问问题。

#### 📝 邮件列表

1. **[06-26 16:20]** [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-08 16:48]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[07-08 19:06]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[07-10 12:48]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

### Thread 2: [GIT PULL] KVM/arm64 fixes for 6.16, take #5

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  3 Jul 2025 11:05:44 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的修复补丁，旨在为 6.16 版本提供更新。

1. **原始 patch/问题的内容**：历史邮件中，Marc Zyngier 提出了一个补丁，主要涉及修复 KVM/arm64 的一些问题，包括移除主机 FPSIMD 状态的 EL1 S1 映射，以及停止向客户机报告错误的 S2 基粒度大小。此外，还修复了未实现粒度大小的 FEAT_GTG 处理。

2. **之前的讨论要点**：在历史讨论中，Marc 提到每周发布一个修复 PR 的趋势，并指出当前修复的严重性逐渐降低。他希望将此补丁与上周的 kvmarm-fixes-6.16-4 PR 一并处理。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Paolo Bonzini 确认补丁将在 KVM 社区会议后提交给 Linus，表明该补丁的进展顺利，预计很快会被合并。

总结来看，此次讨论主要集中在 KVM/arm64 的修复补丁上，历史讨论提供了背景信息，而本周的进展则表明补丁即将被合并。

#### 📝 邮件列表

1. **[07-03 11:05]** [GIT PULL] KVM/arm64 fixes for 6.16, take #5
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-08 16:48]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #5
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

### Thread 3: [GIT PULL] KVM/arm64 fixes for 6.16, take #6

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 11 Jul 2025 09:48:34 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 6.16 版本中的修复，Marc Zyngier 提出了一个补丁，旨在解决嵌套虚拟化中 PMU 寄存器数量的清理问题。补丁的核心内容是修复在调整客机对 MDCR_EL2.HPMN 的视图时对 u64_replace_bits() 的使用。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测出该问题的复杂性以及可能导致的错误影响了虚拟化的稳定性。此次补丁被认为是对之前讨论中提到的“脑筋急转弯”问题的最终修复。

本周的进展是，Marc Zyngier 提交了这一补丁，并请求 Paolo 进行合并。补丁包括对 MDCR_EL2.HPMN 上限的强制执行修复，确保在嵌套虚拟化环境中，客机的寄存器视图能够正确反映。补丁已在 Git 仓库中更新，供相关人员获取。

#### 📝 邮件列表

1. **[07-11 09:48]** [GIT PULL] KVM/arm64 fixes for 6.16, take #6
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 4 个 thread

---

### Thread 1: [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  4 Jul 2025 17:12:55 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 RISC-V 架构的 kvmtool 支持的补丁。历史讨论中，Andrew Jones 提出了两个补丁：第一个补丁确保在非 ARM 主机上运行 kvmtool 时的架构检查，第二个补丁则是为 RISC-V 添加 kvmtool 支持，使其能够作为一流公民运行测试。

在之前的讨论中，Andrew 解释了 kvmtool 在非 ARM 主机（如 x86）上无法正常工作的原因，并强调了 RISC-V 支持的重要性。补丁的代码修改涉及多个文件，添加了必要的检查和支持。

在本周的新讨论中，Jesse Taube 对两个补丁进行了审核并表示支持，同时提出了是否计划为 i386 和 x86_64 添加支持的疑问。Andrew 回复表示目前没有计划，但认为这会是一个好的方向，并提到需要移除与已被弃用的 ARM KVM 相关的代码。Nutty Liu 也对补丁进行了审核，表示赞同。最终，Andrew 确认已将补丁合并，标志着这一支持的实现。

#### 📝 邮件列表

1. **[07-04 17:12]** [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[07-04 17:12]** [kvm-unit-tests PATCH 1/2] arm/arm64: Ensure proper host arch with kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[07-04 17:12]** [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
4. **[07-07 08:10]** Re: [kvm-unit-tests PATCH 1/2] arm/arm64: Ensure proper host arch
 with kvmtool
   - 发件人: Jesse Taube <jesse@rivosinc.com>
5. **[07-07 08:28]** Re: [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Jesse Taube <jesse@rivosinc.com>
6. **[07-07 19:44]** Re: [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
7. **[07-08 11:41]** Re: [kvm-unit-tests PATCH 1/2] arm/arm64: Ensure proper host arch with kvmtool
   - 发件人: Nutty Liu <liujingqi@lanxincomputing.com>
8. **[07-08 11:43]** Re: [kvm-unit-tests PATCH 2/2] riscv: Add kvmtool support
   - 发件人: Nutty Liu <liujingqi@lanxincomputing.com>
9. **[07-08 11:00]** Re: [kvm-unit-tests PATCH 0/2] riscv: Add kvmtool support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 2: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 25 Jun 2025 16:48:00 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 KVM 单元测试中添加 kvmtool 到运行脚本的补丁（PATCH v4 00/13）。该补丁的主要目的是允许用户通过简单的命令配置和运行所有测试，利用 kvmtool 的小巧和易修改性，便于开发者在 KVM 中添加或原型新特性。

在历史讨论中，Alexandru Elisei 提到，kvmtool 默认会尝试确保内核在虚拟机中成功启动，但这可能会对 kvm-unit-tests 造成问题，因为某些测试会解析内核命令行，遇到 kvmtool 添加的额外参数时可能会失败。为了解决这一问题，kvmtool 的一个提交引入了 `--nodefaults` 参数。

在本周的新讨论中，Thomas Huth 提出了在 s390x 上出现的问题，提示 `vmm_defaults_opts` 命令未找到。Andrew Jones 随后回应，指出这个问题已经通过他最近推送的补丁解决。Thomas 对此表示感谢，并为之前未注意到该补丁表示歉意。

总体来看，本周的讨论集中在解决 kvmtool 相关问题的修复上，推动了补丁的进展。

#### 📝 邮件列表

1. **[06-25 16:48]** [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-25 16:48]** [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[07-11 13:32]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Thomas Huth <thuth@redhat.com>
4. **[07-11 16:35]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
5. **[07-11 16:37]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Thomas Huth <thuth@redhat.com>

---

### Thread 3: [syzbot] [kvmarm?] WARNING in pend_sync_exception

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 12 Jul 2025 18:45:31 -0700

#### 🤖 AI 总结

本邮件讨论主题为「[syzbot] [kvmarm?] WARNING in pend_sync_exception」，主要涉及一个在 KVM ARM 虚拟化环境中出现的警告问题。

1. **原始问题**：syzbot 在 Linux 内核的某个提交（15724a984643）中发现了一个警告，具体是在 `pend_sync_exception` 函数中。该警告的详细信息包括 CPU 状态、调用栈等，提示在处理异常时可能存在问题。

2. **之前讨论要点**：本邮件没有提供历史讨论的内容，因此无法总结之前的讨论要点。

3. **本周的新讨论与进展**：本周的邮件由 syzbot 发送，报告了该警告的具体信息，包括相关的内核配置、编译器版本以及重现步骤等。邮件中还附带了可下载的资源，如磁盘镜像和内核映像，以便开发者进行调试和修复。syzbot 提醒开发者在修复该问题后，需在提交中添加相应的标签以便追踪。

总体来看，本周的讨论主要集中在对该警告问题的报告和提供调试信息上，尚未有针对性的解决方案或修复补丁。

#### 📝 邮件列表

1. **[07-12 18:45]** [syzbot] [kvmarm?] WARNING in pend_sync_exception
   - 发件人: syzbot <syzbot+4e09b1432de3774b86ae@syzkaller.appspotmail.com>

---

### Thread 4: [QUESTION] KVM: arm64: Handle FFA_MEM_LEND calls from the host

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 12 Jul 2025 22:55:13 +0900

#### 🤖 AI 总结

本邮件讨论主题为“[QUESTION] KVM: arm64: Handle FFA_MEM_LEND calls from the host”，主要涉及对 KVM 在 arm64 架构下处理 FFA_MEM_LEND 调用的讨论。

1. **原始 patch/问题的内容**：本次讨论围绕一个尚未提供的补丁，意在探讨如何在 KVM 中处理来自主机的 FFA_MEM_LEND 调用。FFA_MEM_LEND 是一种内存借用机制，涉及主机和虚拟机之间的内存管理。

2. **之前的讨论要点**：由于本邮件列表中没有历史讨论，因此没有提供相关的背景信息或之前的讨论要点。

3. **本周的新讨论、进展或结论**：本周的讨论由参与者 daeroro 提出，询问关于补丁的具体实现问题。他关注的是将 FFA_MEM_LEND 视为与 FFA_MEM_SHARE 相同的处理方式是否意味着主机在内存被“借出”后仍然可以访问该内存。这表明对内存访问权限及其影响的关注，可能影响到系统的安全性和稳定性。

总的来说，本周的讨论集中在对补丁实现细节的澄清上，尚未形成明确的结论。

#### 📝 邮件列表

1. **[07-12 22:55]** [QUESTION] KVM: arm64: Handle FFA_MEM_LEND calls from the host
   - 发件人: daeroro <skseofh@gmail.com>

---

